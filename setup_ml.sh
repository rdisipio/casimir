if [ ${HOSTNAME:0:3} == "gra" ]
then
  echo "INFO: Setting up machine learning env on Graham"

  module load cuda/9.0.176
  module load cudnn
  source $HOME/env-ml/bin/activate

  export THEANO_FLAGS=mode=FAST_RUN,device=cuda,floatX=float32,lib.cnmem=1
  echo "THEANO_FLAGS=$THEANO_FLAGS"
fi

alias set_cpu='export THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32,lib.cnmem=1'
alias set_gpu='THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32,lib.cnmem=1'
alias set_gpu0='THEANO_FLAGS=mode=FAST_RUN,device=gpu0,floatX=float32,lib.cnmem=1'
alias set_gpu1='THEANO_FLAGS=mode=FAST_RUN,device=gpu1,floatX=float32,lib.cnmem=1'
alias set_gpu2='THEANO_FLAGS=mode=FAST_RUN,device=gpu2,floatX=float32,lib.cnmem=1'
alias set_gpu3='THEANO_FLAGS=mode=FAST_RUN,device=gpu3,floatX=float32,lib.cnmem=1'

nvidia-smi
