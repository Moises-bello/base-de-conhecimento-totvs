---
article_id: 21864484665751
category: GPE - eSocial - Não Periódicos
content_hash: ca9db5bf5b49b997c95a7c936acee0284e0bbbed72d1934e189cd53db3ef3238
fetched_at: '2026-06-28T22:45:05.821560+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o novo grupo remunAposDeslig
  para Controle de Quarentena
type: support-article
updated_at: '2026-06-16T11:47:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21864484665751-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-novo-grupo-remunAposDeslig-para-Controle-de-Quarentena
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21864484633623) Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Como gerar no S-2299 ou no S-1200 o novo grupo **remunAposDeslig** para **Controle de Quarentena** de acordo com o leiaute S-1.2 do eSocial?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
**Ajuste no cálculo da rescisão para permitir informar o indicativo se haverá pagamento de quarentena na rescisão para ser utilizado na declaração do evento ao eSocial.**  
  
**A melhoria depende da** [**aplicação da atualização liberada no pacote de expedição do módulo RH**](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao) **a partir de 22/12/2023 e da execução do UPDDISTR com o dicionário diferencial para os releases iguais ou superiores a versão 12.1.33.**  
  
No caso de **haver necessidade do pagamento de quarentena**, o usuário deverá efetuar o preenchimento manual na rescisão original dos campos Tp.Rem.Desl. (RG\_TPREMAD) e Dt.Fim.Quar. (RG\_DTQUAR), cujas informações serão enviadas ao eSocial, e deverá efetuar o cálculo de quantas rescisões complementares forem necessárias para efetuar o pagamento das parcelas da quarentena pelo período acordado entre empregador e empregado.

O usuário poderá escolher a melhor forma de efetuar o lançamento dos valores:

1. incluir manualmente o valor da quarentena em **Lançamentos por Funcionário** para os períodos necessários;

2. incluir manualmente o valor da quarentena em **Lançamentos Fixos** para o período acordado;

3. incluir manualmente o valor da quarentena em **Lançamentos Futuros** para o período acordado.

O usuário poderá escolher qualquer verba para efetuar o pagamento da quarentena, mas é necessário configurar o indicativo que trata-se de uma verba para esse pagamento no campo **Ref.Pg.Qua. (RV\_REFQUAR) do Cadastro de Verbas.**  
  
**Exemplo:**  
Cadastro da verba que será utilizada para pagamento da Quarentena deve estar com o campo Ref.Pg.Qua. (RV\_REFQUAR) preenchido:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864515353367)  
  
Verba lançada em **lançamentos futuros** com a quantidade de parcelas que serão pagas para Quarentena, também pode ser lançada em lançamentos por funcionário e lançamentos fixos.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864515355031)  
  
Cálculo da rescisão original, criado os campos Tp.Rem.Desl.(RG\_TPREMAD) e Dt.Fim.Quar.(RG\_DTQUAR), deve ser preenchido com o indicativo de situação de remuneração após o desligamento e a data fim da Quarentena:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864515356567)

**OBS:** O campo data fim será liberado para edição ao preencher o campo Tp.Rem.Desl.

**Rescisão complementar** será calculado a verba lançada para Quarentena e os campos Tp.Rem.Desl.(RG\_TPREMAD) e Dt.Fim.Quar.(RG\_DTQUAR) ficará bloqueado para edição:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864484643223)

**Observação**

1. O sistema não fará validações se foram realizadas todos os pagamentos das parcelas de quarentena ao empregado, nem validará o período de pagamento da quarentena.  
2. Todas as rescisões complementares para a realização desse pagamento deverão ser executadas manualmente pelo usuário.  
3. A rescisão complementar quando ocorre no mês mês da original, gera o evetno S-2299 e quando ocorre em meses posteriores da original, é gerado o evento S-1200.

No **novo grupo foram incluídas as tags**:

**indRemun**  
Indicativo de situação de remuneração após o desligamento.  
Valores válidos:  
1 - Quarentena  
2 - Desligamento reconhecido judicialmente com data anterior a competências com remunerações já informadas no eSocial  
3 - Aposentadoria de servidor com data anterior a competências com remunerações já informadas no eSocial.

**dtFimRemun**  
A data final da quarentena a que está sujeito o trabalhador. No caso de desligamento reconhecido judicialmente ou de concessão de aposentadoria de servidor com data anterior a competências com remunerações já informadas no eSocial, informar o último dia trabalhado

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=809528057)  
[Boletim Controle de Quarentena S-2299](https://tdn.totvs.com/display/public/PROT/DRHROTPRT-9057+DT+Controle+de+Quarentena+S-2299)  
[Boletim Controle de Quarentena S-1200](https://tdn.totvs.com/display/public/PROT/DRHROTPRT-14420+DT+Controle+de+Quarentena+S-1200)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
