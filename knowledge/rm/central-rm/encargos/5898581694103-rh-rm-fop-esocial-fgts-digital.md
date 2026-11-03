---
article_id: 5898581694103
category: Encargos
content_hash: 83016c9aeba520e409e1e9bdf772ebd1d73e40c8ad9536564cc9ff1162dc06d0
fetched_at: '2026-06-28T22:46:52.541187+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - eSocial - FGTS Digital
type: support-article
updated_at: '2026-06-05T17:18:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5898581694103-RH-RM-FOP-eSocial-FGTS-Digital
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16611989546263)*** Tempo aproximado para leitura:**00:03:00 min**  
  
**Dúvida**  
Como será o FGTS Digital e qual o cronograma de implantação do governo?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
O**FGTS Digital** utilizará as informações declaradas pelos empregadores no eSocial para alimentar sua base de dados. O calendário de entrada em produção do novo sistema será divulgado em breve. Enquanto isso, os empregadores devem aproveitar para rever processos internos e conferir se **as informações relacionadas ao FGTS estão sendo declaradas corretamente via eSocial**.

Para isso utilize o **Relatório de Conferência de INSS/FGTS** já disponível na Folha de Pagamento:

* **Cliente Middleware** - [Relatório de Conferência de FGTS](https://tdn.totvs.com/pages/viewpage.action?pageId=536720973)
* **Cliente TAF Padrão** - [Painel de Conferência de FGTS](https://tdn.totvs.com/pages/viewpage.action?pageId=528452163)

Como as informações do eSocial não estavam sendo utilizadas até o momento para realizar recolhimentos, é possível que alguma configuração de incidência de rubricas ou de bases próprias do FGTS não esteja correta.

As empresas devem aproveitar este momento para **rever a forma como fazem a declaração de remunerações atualmente no eSocial**, com destaque para as incidências de FGTS que cadastrou para suas rubricas e fazer os devidos ajustes, se necessário.

Devem **verificar também as verbas remuneratórias que são utilizadas apenas como base para FGTS**, como nos casos de afastamento acidentário, serviço militar obrigatório, aviso prévio indenizado e primeira parcela de 13º salário. O eSocial já fornece totalizadores de FGTS por trabalhador (S-5003) e por empresa (S-5013) para essa conferência.

Neste momento, os empregadores continuam obrigados a **recolher o FGTS pelos sistemas SEFIP/GRRF/Conectividade Social**. Cabe destacar que os recolhimentos de meses anteriores ao FGTS Digital continuarão a ser feitos pelos sistemas da CAIXA.

**- Cronograma de implantação**

Conforme dito acima, a data de implantação do FGTS Digital será divulgada em breve. Quando for divulgada a data de implantação do FGTS Digital, os empregadores terão cerca de 06 meses para ajustar seus processos internos e conhecer melhor o sistema. Inclusive, será disponibilizado um ambiente de testes (**produção limitada**), onde os empregadores poderão**visualizar os dados reais declarados via eSocial e como aparecem no FGTS Digital**, além de **simular a emissão de guias**.

![](https://tdn.totvs.com/download/attachments/630000929/image-2023-12-6_13-47-16.png?version=1&modificationDate=1701881236943&api=v2)

**- Sincronismo entre eSocial x FGTS Digital**

O envio de admissões, alterações cadastrais e contratuais, desligamentos e remunerações - principalmente - terão **impacto quase simultâneo** na gestão e geração de guias e outros serviços do sistema. A cada evento transmitido do trabalhador, haverá a sensibilização no FGTS Digital. **Não será necessário fechar a folha de pagamento (evento S-1299) para que o empregador possa gerar guias de determinada competência (mês)**. Em dias de grande volume de dados transmitidos, poderá haver um intervalo maior de tempo entre o envio e o processamento interno do FGTS Digital. E o empregador deve certificar-se de que todas as remunerações transmitidas já constam na tela. Para simplificar esse processo, principalmente para empresas com elevado número de trabalhadores, quando o empregador enviar o evento de fechamento da folha (S-1299), o FGTS Digital fará uma validação interna para verificar se todas as remunerações recebidas coincidem com o totalizador do FGTS (S-5013). Após essa verificação, o sistema indicará o status da folha (fechada ou aberta) e o horário em que foi realizada aquela validação.

As retificações de remunerações também terão impacto no eSocial. Se o empregador informar uma remuneração com valor errado, ou utilizar rubrica equivocada, poderá fazer a correção no eSocial, que enviará os novos dados para o FGTS Digital. Caso o empregador já tenha realizado o recolhimento/pagamento da guia, poderá pagar apenas a diferença - se tiver declarado uma remuneração maior que a anterior - ou pedir a restituição/compensação de valores.

Sempre que possível, o FGTS Digital fará a compensação entre valores pagos e retificados numa mesma competência, para evitar que a empresa tenha que fazer um pedido para isso. Caso seja necessário um pedido formal do empregador, tudo será feito de forma online e com transparência.

**Importante**  
Através da plataforma do FGTS Digital será gerada a **GFD - Guia FGTS Digital**para recolhimento do FGTS, que substituirá a guia SEFIP e GRRF.

No [Portal do FGTS Digital](https://gov.br/fgtsdigital) poderá acessar as principais notícias e informações sobre o futuro processo de recolhimento, que passará a ser feita por meio da ferramenta tecnológica PIX.

Em breve iremos evoluir nossa Folha de Pagamento para que seja possível gerar o lançamento financeiro da Guia FGTS Digital.

Acompanhem as publicações que são divulgadas através do[**RH Informa**](https://rhinforma.totvs.com/).  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Novidades eSocial](https://tdn.totvs.com/display/public/LRM/Novidades+eSocial+-+Linha+RM)  
     - [FGTS Digital](https://www.youtube.com/watch?v=Pkkln2Au4G8)  
     - [FGTS Digital - Tratativa quando há base negativa de FGTS e/ou FGTS 13o. Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=832650111)  
     - [Remuneração para fins rescisórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17887407781271-RH-RM-FOP-eSocial-FGTS-Digital-Remunera%C3%A7%C3%A3o-para-fins-rescis%C3%B3rios)   
     - [Recolhimento da Multa Rescisória CNPJ Raiz ou CNO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23698036880535-RH-RM-FOP-eSocial-FGTS-DIGITAL-Recolhimento-da-Multa-Rescis%C3%B3ria-CNPJ-Raiz-ou-CNO)   
     - [Base de cálculo da indenização compensatória - Multa do FGTS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17648197908247-RH-RM-FOP-eSocial-Base-de-c%C3%A1lculo-da-indeniza%C3%A7%C3%A3o-compensat%C3%B3ria-Multa-do-FGTS)
