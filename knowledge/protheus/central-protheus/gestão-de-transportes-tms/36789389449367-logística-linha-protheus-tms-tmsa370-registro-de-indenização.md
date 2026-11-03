---
article_id: 36789389449367
category: Gestão de Transportes (TMS)
content_hash: bc9c515e5e9f69ad38f03fc0244139f4b77cfa40c96a880ebf770d71f0e36670
fetched_at: '2026-06-28T22:45:33.422806+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - TMSA370 - Registro de Indenização
type: support-article
updated_at: '2026-04-13T12:33:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36789389449367-Log%C3%ADstica-Linha-Protheus-TMS-TMSA370-Registro-de-Indeniza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36789389438743) Tempo aproximado para leitura: **00:05:00min**  
  
**Dúvida**  
Como ocorre o apontamento de ocorrências do tipo Gera Indenização e Estorna Indenização?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**  
Indenização é a reparação devida ao segurado, seja de uma avaria, perda ou roubo de carga, a qual será paga em dinheiro ou em reposição do bem. O objetivo desta rotina é controlar os registros de indenizações geradas ao embarcador da carga, podendo autorizar, ou não, o seu pagamento.  
Através do **Registro de Ocorrências - TMSA360** é possível registrar uma ocorrência do tipo **Gera Indenização** ou até mesmo através do **Registro de Pendências - TMSA540**, transformando o processo numa pendência com indenização.  
  
Após registrar uma ocorrência do tipo **Gera Indenização**, será criado um registro na rotina **Registro de Indenização - TMSA370**, onde será feito o processo para ser indenizado pelo Faturamento.  
O registro permanecerá em aberto até que o título da indenização tenha sido baixado na rotina **Funções** **Contas a Pagar -** **FINA750**.  
Para tratar casos em que não haverá o pagamento da indenização, como, por exemplo, em situação de extravio de mercadoria que, posteriormente, foi encontrada a carga, podem ser utilizadas as opções:

* Encerramento do registro de indenização;
* Estorno do encerramento do registro de indenização.

Após registrar a ocorrência, o Sistema criará um registro no programa **TMSA370 - Registro de Indenização.** Esta **f**uncionalidade possui os seguintes processos:

**Autoriza Pagto:** Permite autorizar o pagamento de indenizações, gerando no **Contas a Pagar** um título com o valor a ser pago.  
  
**Estorna Pagto:** Permite estornar a autorização do pagamento de indenizações, excluindo no **Contas a Pagar** o título gerado para a indenização.  
  
**Status Financeiro:** Permite alterar o status dos registros de indenização já pagos para **Encerrado**, ou seja, ao executá-la, será verificado se os títulos relacionados às indenizações estão baixados - pagos.  
  
**Encerrar:** Permite encerrar o registro de indenização que estiver na situação **Em Aberto**.  
  
**Estornar Encerramento:** Permite desfazer o encerramento de um registro não indenizado.   
  
O Status dos registros são identificados da seguinte forma:

![image (18).png](https://centraldeatendimento.totvs.com/hc/article_attachments/39660627657879)

Para manutenir os registros de indenizações:  
Em **Registro de Indenização - TMSA370,** posicione sobre o registro desejado e clique em **Alterar**.  
É apresentada a tela **Registro de Indenizações - Alterar**, dividida em áreas:

* **Cabeçalho:** Nesta área, são apresentados os dados da ocorrência que gerou o registro (filial, data, hora, ramo de seguro, viagem, ocorrência, motivo, etc.) e os dados relacionados à indenização (número do registro de indenização, número do processo, etc).
* **Itens**: Nesta área, são apresentados os dados relacionados à indenização, tais como: status da indenização (em aberto, pagamento autorizado, encerrado), status do reembolso (em aberto, solicitado, reembolsado, sem reembolso), documento, cliente, quantidade do documento, quantidade da ocorrência, percentual de seguro do cliente, valor da carga, valor do prejuízo com base no percentual de seguro do cliente, valor a indenizar, data de vencimento da indenização, número do certificado de vistoria, etc.
* **Rodapé:** Exibe os valores totais relacionados à indenização, tais como: total da carga, total indenização, total indenizado, saldo a indenizar, etc

Na manutenção o Sistema permite alterar apenas alguns campos dos itens, sendo eles: código do cliente, **Valor do Prejuízo -** **DUB\_VALPRE**, **Data de Vencimento da Indenização -** **DUB\_DATVEN** e **Certificado de Vistoria -** **DUB\_CERVIS**.  
  
Para verificar os detalhes da viagem de transporte, clique em Viagem ou F4 conforme imagem:

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39026622790935)

Após salvar os dados o Sistema atualiza automaticamente o campo **Vl.Indenizar - DUB\_VALIND**.  
  
Para autorizar o pagamento da indenização, utilize a opção **Autoriza Pagamento**.  
Na autorização do pagamento, ao confirmar a autorização é gerado no **Contas a Pagar** um título com o valor a ser pago conforme os dados informados na manutenção do registro. O registro de indenização será apresentando com o status **Pagamento Autorizado**.  
O principal parâmetro de uso da funcionalidade é o **MV\_TMSFATU**, permitindo na geração de um título a pagar, considerar a filial atual ao invés da filial que consta no registro de indenizações.  
  
No estorno de autorização de pagamento ao confirmar o estorno do pagamento da indenização, é excluído o título gerado no **Contas a Pagar** referente a indenização, alterando o status do registro de indenização para E**m Aberto.**  
  
Para encerrar o registro de indenização, poderá ser feito de duas formas: pela validação do **Contas a Pagar** e a outra somente pelo **TMS**.  
  
Para validar pelo **Contas a Pagar**: No registro, clique em **Outras Ações** > **Status Financeiro** > **OK**, após a confirmação, o Sistema apresenta uma mensagem de alerta informando o total de títulos baixados relacionados às indenizações.  
Se o total de títulos baixados for diferente de 0 (zero) significa que foram pagos títulos referentes as indenizações, encerrando os respectivos registros.  
  
Para validar apenas pelo **TMS**: No registro, clique em **Outras Ações** > **Encerrar**. Na sequência é apresentada uma tela para o encerramento do registro de indenização. No campo **Motivo** informe uma justificativa para o encerramento em questão.  
  
Confira os dados e confirme. O status deste registro permanecerá como **Encerrado** - Não Indenizado.  
Em casos em que o registro fica com situação de Encerrado - Não Indenizado é possível estornar o encerramento, em **Outras Ações** > **Estornar Encerramento** > **Confirmar**.   
  
**Saiba mais**  
Para mais detalhes sobre os demais processos da rotina, verifique a documentação [Registro de Indenização (TMSA370 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=465393436).  
Verifique também a documentação da rotina [Registro de Pendências (TMSA540 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=505769714), nesta rotina, também é possível gerar o **Registro de Indenização**.  
  
**Anexos**  
Vídeo simulando o processo de registro de indenização, pagamento no **Contas a Pagar** e encerramento da indenização.
