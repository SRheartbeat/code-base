try:
    from tensorboardX import SummaryWriter
    is_tensorboard_available = True
except Exception:
    is_tensorboard_available = False

logging.basicConfig(
    format='[%(asctime)s %(name)s %(levelname)s] - %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
  
    train_name = time.strftime("%m%d_%H%M%S", time.localtime())
    train_name = ('DeepCrack_' + 'crack206' + '_%dx%d_' + train_name) % (512, 512)

    # visble
    if is_tensorboard_available:
        log_writer = SummaryWriter(join(cfg.checkpoint, train_name, "log"))  # 运行到这里，会创建log文件夹
        with open(join(cfg.checkpoint, train_name, "log", "config.txt"), 'w') as f:
            f.write(cfg.__str__())
    else:
        log_writer = None
        
    log_writer.add_scalar('train_total_loss', trainer.log_loss['total_loss'], train_loss_step)
