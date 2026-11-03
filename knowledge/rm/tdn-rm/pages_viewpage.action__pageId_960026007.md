---
content_hash: 8888117fae3bdb73f7ef7bb83bd89f446c223df3baac0bf9420aa8b0b5c28e64
fetched_at: '2026-06-29T00:12:13.493494+00:00'
page_id: '960026007'
product: rm
source: tdn-rm
title: Fracionamento de jobs inteligente (Movimento por regime de caixa)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=960026007
version: 5
---

A partir das versões **12.1.2410.261,  12.1.2502.164, 12.1.2506.106**, foi disponibilizado o fracionamento de jobs inteligente para Geração de movimento por regime de caixa.

Com o parâmetro de "**Fracionamento de Jobs Inteligente**" ativo: O Fracionamento Inteligente é acionado durante a **Geração de movimento por regime de caixa**. É realizado um cálculo para obter o número de frações permitindo que os jobs sejam finalizados em menor tempo.

Importante

É importante ressaltar que o fracionamento só é acionado durante a geração de movimento. O processo de cancelamento e exclusão não utilizam o fracionamento inteligente.

O fracionamento de jobs inteligente, está programado para funcionamento apenas em ambiente que tenha suporte a execução com mais de 20 jobs em paralelo.

No modelo atual de fracionamento de jobs usando valores fixos, cada requisição é sempre dividida no número de frações pré-estabelecido através das configurações do sistema, independente da quantidade de movimentos envidados para processamento. Isso gera um tempo de execução proporcional a carga por fração. Fazendo com que solicitações com grandes quantidades sejam fracionadas usando menos frações do que poderiam, prolongando o tempo de execução total.

**O fracionamento de jobs inteligente** é adaptado proporcionalmente a quantidade de boletos envida para geração de movimento, quanto maior a quantidade mais frações serão usadas. Foi usado o limite de 30% do número máximo de frações suportado pelo ambiente, o que deve proporcionar um aproveitamento melhor da capacidade do sistema sem gerar impacto em outros processos.

## Configurando fracionamento de jobs inteligente:

1. *Configurações / Parâmetros / Integração / Fiscal / Fiscal 1/2*

Ao marcar o parâmetro de "**Habilita o fracionamento de jobs inteligente na geração de movimento por caixa**", um alerta informando os limites relacionados a quantidade mínima de geração de 20 frações em paralelo é exibido:

Com o parâmetro marcado, ao executar a Geração de movimento por caixa, a quantidade de frações pode ser calculada automaticamente não respeitando o valor informado no processo.

Mensagem informando que a quantidade de jobs informada na solicitação pode não ser respeitada.

Importante!

A partir da versão **12.1.2506** foi criada a possibilidade de definir a quantidade de registros processados por cada JOB do fracionamento. Para defini-lo, deve ser criado um registro em **Rotinas Fiscais**, com um **Parâmetro da rotina** com código **TAMANHO\_FRACIONAMENTO** e seu **Valor** , conforme mostrado na imagem abaixo.

Por padrão, o processo considera o fracionamento a cada 100 registros, e limita a 1000 registros, mesmo que o valor seja definido maior.
