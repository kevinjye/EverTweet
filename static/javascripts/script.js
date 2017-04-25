// var startDate = '';
// var endDate = '';
var numTweets = '';
var twitterHandle = '';

// $("#startDate").change(function(){
//     startDate = $('#startDate').val();
//     if ((startDate != '') && (endDate != '') && (twitterHandle != '')){
//         console.log(twitterHandle, startDate, endDate)
//         get_data(twitterHandle, startDate, endDate)
//     }
// })

// $("#endDate").change(function(){
//     endDate = $('#endDate').val();
//     if ((startDate != '') && (endDate != '') && (twitterHandle != '')){
//         console.log(twitterHandle, startDate, endDate)
//         get_data(twitterHandle, startDate, endDate)
//     }
// })

$("#numTweets").change(function(){
    numTweets = $('#numTweets').val();
    if ((numTweets != '') && (twitterHandle != '')){
        console.log(twitterHandle, numTweets)
        get_data(twitterHandle, numTweets)
    }
})

$("#twitterHandle").change(function(){
    twitterHandle = $('#twitterHandle').val();
    if ((numTweets != '') && (twitterHandle != '')){
        console.log(twitterHandle, numTweets)
        get_data(twitterHandle, numTweets)
    }
})


// some examples: ishantlguru, realDonaldTrump, justinbieber
get_data('BarackObama', '10');

function get_data(twitterHandle, numTweets) {
    $('#container').append('<div style="height: 800px" id="total_chart"></div>');

    // $.getJSON('https://www.highcharts.com/samples/data/jsonp.php?filename=usdeur.json&callback=?', function (data) {
    $.getJSON('/getSentimentList/' + twitterHandle + '/' + numTweets, function (data) {
    // $.getJSON('/getSentimentList/therealjamesxue', function (data) {

        console.log(data)

        series_list = []

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

        new_data_fear = []
        for (index in data['fear']){
            new_data_fear.push(data['fear'][index].slice(1, 3))
        }

        new_data_disgust = []
        for (index in data['disgust']){
            new_data_disgust.push(data['disgust'][index].slice(1, 3))
        }

        series_list.push({
            type: 'line',
            name: 'Angry',
            color: '#EC4422',
            data: new_data_angry
        })

        series_list.push({
            type: 'line',
            name: 'Joy',
            color: '#F8E250',
            data: new_data_joy
        })

        series_list.push({
            type: 'line',
            name: 'Sadness',
            color: '#2A58A5',
            data: new_data_sadness
        })

        series_list.push({
            type: 'line',
            name: 'Fear',
            color: '#8258A2',
            data: new_data_fear
        })

        series_list.push({
            type: 'line',
            name: 'Disgust',
            color: '#73BB4B',
            data: new_data_disgust
        })

        console.log(series_list);

        create_chart(twitterHandle);
    });
}


 function create_chart(twitterHandle) {
        
        Highcharts.chart('container', {
            chart: {
                zoomType: 'x'
            },
            title: {
                text: 'Tweet Sentiment Data for @' + twitterHandle + ' over time'
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