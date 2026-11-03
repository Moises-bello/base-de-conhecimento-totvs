---
article_id: 5217479833623
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: b756f36565b19dc4052a00a80ea6c4c1e1c287ea530ae5f218df21378c8a7da9
fetched_at: '2026-06-28T22:37:21.323235+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao encerrar uma medição
  de contrato o sistema apresenta a mensagem - HELP - AJUDA:OBRIGAT - Um ou mais campos
  obrigatórios não foram preenchidos-> C. Custo
type: support-article
updated_at: '2025-12-24T11:33:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5217479833623-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-encerrar-uma-medi%C3%A7%C3%A3o-de-contrato-o-sistema-apresenta-a-mensagem-HELP-AJUDA-OBRIGAT-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-C-Custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37242724470167) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
**Quando vou realizar a medição de um contrato que gere titulo, o sistema me apresenta a mensagem de HELP - AJUDA:OBRIGAT - Um ou mais campos obrigatórios não foram preenchidos-> C. Custo**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - desde Release 12.1.25  
  
**Causa**  
***Nessa mensagem existem duas condições que podem gerar o erro:***

***1-** Possuir o campo de centro de custo da CNE-> CNE\_CC como obrigatório.*

***2-** Possuir o campo de centro de custo da SE2-> E2\_CCUSTO / SE1-> E1\_CCUSTO como obrigatório e sua medição de contrato gerar titulo financeiro.*  
  
**Solução:**

***1.** No primeiro caso, devera verificar todas as linhas dos itens que constam no contrato, e verificar se os mesmos possuem o campo de centro de custo preenchido, caso contrato preencha com o centro de custo correto.*

***2.** No segundo caso, deve verificar se na tabela SE2 o campo de centro de custo E2\_CCUSTO foi marcado como obrigatório (Ou E1\_CCUSTO, no caso de Contrato de Venda que gera Titulo a Receber), e assim ao finalizar uma medição, o titulo alerta informando na rotina CNTA121 que o campo de centro de custo não esta sendo preenchido.*

***Obs:***

Deve se atentar que os títulos gerados pelo GCT não carregam informações como centro de custo, pois o campo de centro de custo do titulo não é especifico para o GCT e sim preenchido por todo o Protheus. Caso deseje preencher o centro de custo de forma automática, deve utilizar os pontos de entrada abaixo:

**Pontos de Entrada que podme ser utilizados para tratar situação acima:**

**N120VENC :** [CN120VENC - Encerramento da medição](https://tdn.totvs.com/pages/releaseview.action?pageId=6089573)

**CTA120FN :**[CNT121PC - Chamado antes da geração do pedido de compra para realizar customizações](https://tdn.totvs.com/pages/viewpage.action?pageId=271385334)

**MD130GRV :**[MD130GRV - Medição do contrato](https://tdn.totvs.com/pages/releaseview.action?pageId=6089632)

**CN121AFN:** [CN121AFN - Altera informações do título financeiro no encerramento da medição](https://tdn.totvs.com/pages/viewpage.action?pageId=578632647)

***Saiba Mais:***

[MP - SIGAGCT - Pontos de entrada para rotinas de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-MP-SIGAGCT-Pontos-de-entrada-para-rotinas-de-Medi%C3%A7%C3%A3o?source=search)

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
