/**
 * renders pdf attachment on to the chat screen
 * @param {Object} pdf_data json object
 */
function renderVideoAttachment(video_data) {
    const { url: video_url } = video_data.custom;
    const { title: video_title } = video_data.custom;
    const video_attachment = `<div class="pdf_attachment"><div class="row"><div class="col s3 pdf_icon">
<i class="fa fa-file-video-o" aria-hidden="true"></i></div><div class="col s9 pdf_link"><a href="${video_url}" target="_blank">
${video_title} </a></div></div></div>`;

    $(".chats").append(video_attachment);
    scrollToBottomOfResults();
}
