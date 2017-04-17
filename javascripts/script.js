var startDate = '';
var endDate = '';
var twitterHandle = '';

$("#startDate").change(function(){
    startDate = $('#startDate').val();
    if ((startDate != '') && (endDate != '') && (twitterHandle != '')){
        console.log(twitterHandle, startDate, endDate)
        create_graph(twitterHandle, startDate, endDate)
    }
})

$("#endDate").change(function(){
    endDate = $('#endDate').val();
    if ((startDate != '') && (endDate != '') && (twitterHandle != '')){
        console.log(twitterHandle, startDate, endDate)
        create_graph(twitterHandle, startDate, endDate)
    }
})

$("#twitterHandle").change(function(){
    twitterHandle = $('#twitterHandle').val();
    if ((startDate != '') && (endDate != '') && (twitterHandle != '')){
        console.log(twitterHandle, startDate, endDate)
        create_graph(twitterHandle, startDate, endDate)
    }
})

create_graph('01/01/2016', '04/16/2017')

function create_graph(twitterHandle, startDate, endDate) {
    $('#container').append('<div style="height: 800px" id="total_chart"></div>');

    $.getJSON('https://www.highcharts.com/samples/data/jsonp.php?filename=usdeur.json&callback=?', function (data) {
        console.log(data);

        series_list = []
        series_list.push({
            type: 'line',
            name: 'Anger',
            color: '#BF0B23',
            data: data.slice(0, 300)
        })

        series_list.push({
            type: 'line',
            name: 'Happiness',
            color: '#008000',
            data: data.slice(301, 500)
        })

        series_list.push({
            type: 'line',
            name: 'Sadness',
            color: '#0000ff',
            data: data.slice(501, 600)
        })


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
    });
}