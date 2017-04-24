var startDate = '';
var endDate = '';
var twitterHandle = '';

$("#startDate").change(function(){
    startDate = $('#startDate').val();
    if ((startDate != '') && (endDate != '') && (twitterHandle != '')){
        console.log(twitterHandle, startDate, endDate)
        get_data(twitterHandle, startDate, endDate)
    }
})

$("#endDate").change(function(){
    endDate = $('#endDate').val();
    if ((startDate != '') && (endDate != '') && (twitterHandle != '')){
        console.log(twitterHandle, startDate, endDate)
        get_data(twitterHandle, startDate, endDate)
    }
})

$("#twitterHandle").change(function(){
    twitterHandle = $('#twitterHandle').val();
    if ((startDate != '') && (endDate != '') && (twitterHandle != '')){
        console.log(twitterHandle, startDate, endDate)
        get_data(twitterHandle, startDate, endDate)
    }
})

get_data('01/01/2016', '04/16/2017')

function get_data(twitterHandle, startDate, endDate) {
    $('#container').append('<div style="height: 800px" id="total_chart"></div>');

    // $.getJSON('https://www.highcharts.com/samples/data/jsonp.php?filename=usdeur.json&callback=?', function (data) {
    $.getJSON('/getSentimentList/ishantlguru', function (data) {
        console.log(data);

        series_list = []
        seriesCounter = 0,
        names = ['Angry', 'Joy', 'Sadness'];

        new_data_angry = []
        for (index in data['angry']){
            new_data_angry.push(data['angry'][index].slice(1, 3))
        }

        new_data_joy = []
        for (index in data['joy']){
            new_data_joy.push(data['joy'][index].slice(1, 3))
        }

        new_data_sadness = []
        for (index in data['sadness']){
            new_data_sadness.push(data['sadness'][index].slice(1, 3))
        }

        series_list.push({
            type: 'line',
            name: 'Angry',
            color: '#BF0B23',
            data: new_data_angry
        })

        series_list.push({
            type: 'line',
            name: 'Joy',
            color: '#008000',
            data: new_data_joy
        })

        series_list.push({
            type: 'line',
            name: 'Sadness',
            color: '#0000ff',
            data: new_data_sadness
        })

        console.log(series_list);


        create_chart();
    });
}


 function create_chart() {
        
        Highcharts.chart('container', {
            chart: {
                zoomType: 'x'
            },
            title: {
                text: 'Tweet Sentiment Data for user over time'
            },
            subtitle: {
                text: document.ontouchstart === undefined ?
                        'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                title: {
                    text: 'Sentiment Score'
                }
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: {
                            x1: 0,
                            y1: 0,
                            x2: 0,
                            y2: 1
                        },
                        stops: [
                            [0, Highcharts.getOptions().colors[0]],
                            [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                        ]
                    },
                    marker: {
                        radius: 2
                    },
                    lineWidth: 1,
                    states: {
                        hover: {
                            lineWidth: 1
                        }
                    },
                    threshold: null
                }
            },

            series: series_list
        });
}