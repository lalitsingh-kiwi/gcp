### Deployment
    gcloud functions deploy hello_gcp_pub_sub --memory=512 --runtime python37 --trigger-topic hello-gcp-pub-sub --service-account=lead-comment-activity-sa@leasera-200719.iam.gserviceaccount.com
    
### Topic name
    projects/leasera-200719/topics/hello-gcp-pub-sub