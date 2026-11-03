---
article_id: 1500007681042
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: beeae6e0a2787ca5adc19d910117ec3b1c9745bba5909b4dfa7e41d09d009566
fetched_at: '2026-06-28T22:39:50.027420+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Complemento de
  valor para itens do processo de importação
type: support-article
updated_at: '2024-11-29T16:54:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007681042-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Complemento-de-valor-para-itens-do-processo-de-importa%C3%A7%C3%A3o
---

**Dúvida**Como incluir o Complemento de Valor para Itens do Processo de Importação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011143441)**

#### **Procedimento para Utilização**

* Possuir um processo de importação com despesas Base de custo incluídas no processo
* Utilizar um importador para o processo conforme configurado o estado no parâmetro **MV\_EIC0063**

**Sequencia 01:**

1. Acesse o modulo “Estoque/Custo” e clique em “Atualizações /Cadastros / Movimentações / Internas”
2. Inclua um novo tipo de movimentação seguindo as seguintes informações: Tipo de TM (F5\_TIPO) = Devolução, Aprop.Indir.(F5\_APROPR) = Sim, Atu.Empenho (F5\_ATUEMP) = Não, Transf.MOD.(F5\_TRANMOD) = Não, Valorizado (F5\_VAL) = Sim, Qtd Zero (F5\_QTDZERO) = Sim.

**Sequencia 02:**

1. No Easy Import Control (SIGAEIC), acesse “Atualizações / Desembaraço / Receb. Importação”, selecione o processo de importação e clique em “Ações Relacionadas / Única”.
2. Veja que foi apresentado uma mensagem informativa, dizendo que Para o Estado do importador - SP - as despesas nacionais base de custo foram configuradas para serem utilizadas na rotina de "Complemento de valor" e serão desconsideradas pelo sistema. Clique em Ok.
3. O sistema irá a partir deste momento realizar a geração da nota fiscal seguindo o da nota fiscal Primeira. Gere a nota fiscal para os itens do processo.
4. Acesse a rotina de Despesas na manutenção do desembaraço. Observe que há despesas sem numero de nota fiscal que são as despesas base de custo que foram descartadas pelo sistema no processo de geração da nota fiscal.
5. Acesse novamente a rotina de recebimento de importação e clique em “Ações Relacionadas / Complementar”.
6. Veja que o sistema apresentou a mensagem “Para a geração do complemento de valor das despesas base de custo, utilize a rotina ‘Complemento de Valor’.”

**Sequencia 03:**

1. Clique em “Ações Relacionadas / Complemento de valor / Gerar”. Veja que é aberto a tela de geração do complemento de valor e apenas é apresentado no canto superior direito as despesas que são base de custo e que foram descartada na geração da nota fiscal Única e Complementar.
2. Nesta nova rotina é apresentado no canto superior esquerdo as informações do processo e os novos campos de Numero Documento, Tipo de Movimento e Centro de custo. Do lado esquerdo é mostrado as despesas base de custo utilizadas no rateio dos valores para os itens e na parte inferior os itens do processo.
3. Para realizar a geração é necessário ter cadastrado um tipo de movimento.
4. Na rotina de complemento de valor, é necessário e obrigatório o preenchimento dos campos Numero Documento e Tipo de Movimento. Quando o campo Centro de custo estiver vazio o sistema apresentará uma mensagem informando se deseja enviar o centro de custo associado ao item do processo. Na parte inferior é possível a seleção de quais itens deseja enviar na integração de complemento de valor com o modulo de estoque/custo.
5. Apenas os itens selecionados terão a integração de valor enviados para o modulo de estoque/custo pois entendesse que estes são itens de estoque. Os demais itens ainda que não transmitidos terão os seus valores proporcionais de custo registrados apenas no modulo *Easy Import Control* para histórico.
6. Após o processamento a tela permanecerá aberta mas apenas em modo de visualização, com os campos Numero Documento, Tipo de Movimento e Centro de custo bloqueados para alteração.
7. Clique na opção de “Visualização”, “Complemento de Valor / Visualizar”. Veja que é apresentado o processo e os itens que foram integrados, é informado o campo Sequencial (WN\_NUMSEQ) preenchido com a referencia gerada na rotina de movimentações internas no modulo estoque/custo.

**Sequencia 04:**

1. Acesse o modulo Estoque/Custos, clique em “Atualizações / Movimentações / Internas / Movim. Múltipla”. Veja que existe uma movimentação com o mesmo código de Documento que foi gerado pelo SIGAEIC.
2. Selecione e clique em Visualizar, veja que apenas foi integrado o valor do rateio das despesas, o campo quantidade está vazio. Caso tente realizar o estorno deste documento o sistema informará que ele foi originado pela importação e deve ser estornado na origem.
3. No modulo *Easy Import Control*, acesse a rotina de Despesas na manutenção do desembaraço e inclua uma nova despesa base de custo para o processo. Após a inclusão repita novamente a geração do complemento de valor.
4. No modulo Estoque/Custos, acesse a rotina “Atualizações / Movimentações / Internas / Movim. Múltipla”, veja que foi integrado o novo documento originado pelo *Easy Import Control.*
5. No modulo *Easy Import Control*, acesse a rotina de complemento de valor, estornar. Veja que é apresentado uma tela com documentos de complemento de valor integrados com o estoque/custo.
6. Selecione um documento e clique em confirmar. Clique em confirmar para realizar o estorno.
7. No modulo Estoque/Custo, na rotina “Atualizações / Movimentações / Internas / Movim. Múltipla”, veja que foi incluído um novo registro com o tipo de movimento “999” que significa estorno com o mesmo numero do documento que foi integrado pelo *Easy Import Control.* Eles estaram com o Status de estornados com um “X” vermelho a frente dos dois.
8. Após realizar o estorno pela rotina de Complemento de valor, as despesas estarão disponíveis novamente para serem utilizadas na integração.

**Sequencia 05 - Despesas Base de ICMS:**

**Configuração:**

* MV\_ICMSNFC = .T.
* Ter uma despesas Base de Icms com o campo ICMS na NFC?(YB\_ICMSNFC) = Sim.
* Caso tenha a necessidade de utilizar despesas base de icms na nota fiscal complementar, observe os procedimentos complementares.

1. Inclua uma nova despesa no processo que seja base de icms e acesse novamente a rotina de nota complementar.
2. Ao clicar na rotina de nota complementar, o sistema irá apresentar a mensagem “Deseja calcular I.C.M.S. para a Nota Fiscal Complementar.”, esta é uma validação já existente no processo. Clique em Não. Veja que novamente é apresentado a mensagem de validação para as despesas base de custo.
3. Após gerar a nota complementar a rotina irá desconsiderar as despesas que são Base de ICMS
4. clique em “Ações Relacionadas / Complemento de Valor / Gerar”. Nesta nova rotina é apresentado no canto superior esquerdo as informações do processo e os novos campos de Numero Documento, Tipo de Movimento e Centro de custo. Do lado esquerdo é mostrado as despesas base de custo utilizadas no rateio dos valores para os itens e na parte inferior os itens do processo.
5. Clique em cancelar, e gere a nota fiscal complementar dessa vez clicando em SIM na mensagem “Deseja calcular I.C.M.S. para a Nota Fiscal Complementar.” Veja que após clicar em sim o sistema apresenta uma nova mensagem informando que “Foram identificadas despesas base de custo para o processo. Estas despesas serão desconsideradas na geração da nota fiscal complementar. Para estas despesas utilize a rotina “Complemento de Valor”.

**Sequencia 06 - Geração do complemento de valor com alteração de armazém:**

**Configuração:**

* No módulo SIGAEST (Estoques) é necessário cadastrar um saldo inicial dos produtos em dois armazéns, onde o saldo inicial destes produtos sejam maiores que suas quantidades no processo de importação/nota fiscal de entrada. Para acessar a rotina de cadastro de saldo inicial no módulo de Estoques (SIGAEST) acesse a rotina: Atualizações > Saldos > Inicial. Para cada produto de código distinto no processo de importação, é necessário incluir o saldo inicial nos dois armazéns que serão utilizados no teste da funcionalidade de alteração de armazém dentro da geração do complemento de valor no SIGAEIC.

1. Acessar Atualizações > Desembaraço > Receb. Importação.
2. Selecionar processo de importação desejado e clicar no botão Outras Ações > Complemento de Valor > Gerar.
3. Na sessão "Movimento Interno" informar o tipo de movimento .
4. Na sessão "Alteração de Armazém", informar o campo "DE:" com um código válido e que esteja relacionado à pelo ao menos um item da nota fiscal marcado para integrar.
5. Na sessão "Alteração de Armazém", informar o campo "PARA:" com um código válido (será o armazém de destino do item).
6. Na sessão "Alteração de Armazém", clicar no botão "Alterar". Sistema irá alterar os armazéns para os itens que atenderem Às condições de alteração e irá exibir mensagem informativa de sucesso ao final do processamento.
7. Clicar no botão Confirmar da rotina. Sistema irá exibir a tela relativo a informação do Centro de Custo a ser utilizado na geração da NF de Complemento de Valor.
8. Sistema irá exibir a tela relativo a informação do Centro de Custo a ser utilizado na geração da NF de Complemento de Valor.
9. Clicar no botão "Sim" para utilizar o centro de custo associado ao item do processo. Sistema deve exibir a tela de processamento concluído com sucesso.  
   Os campos e botões das sessões "Movimento Interno" e "Alteração de Armazém" ficarão desabilitados para alteração.  
   No browser inferior, a coluna "Status" deve ser atualizada com o valor "Integrado" para todos os itens marcados.
10. Clicar no botão "Fechar" da mensagem e em seguida no botão "Cancelar" para encerrar a rotina.

**Saiba mais: [Complemento de Valor para Itens do Processo de Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=235584195)  
[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Descontinuação do parâmetro "MV\_EIC0062".](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18495986133399-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Descontinua%C3%A7%C3%A3o-do-par%C3%A2metro-MV-EIC0062)**
