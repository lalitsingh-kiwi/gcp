# gcp

gcloud kms encrypt \
  --plaintext-file=.env.yaml \
  --ciphertext-file=.env.yaml.enc \
  --location=global \
  --keyring=Envs \
  --key=hello-gcp-1-env
  