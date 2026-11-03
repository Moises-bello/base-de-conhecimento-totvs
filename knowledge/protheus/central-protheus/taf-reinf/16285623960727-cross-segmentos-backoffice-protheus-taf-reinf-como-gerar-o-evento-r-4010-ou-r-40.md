---
article_id: 16285623960727
category: TAF - REINF
content_hash: 80713a5a896db518807391a303781fd0754dabb8407c67c33105318be5966b9a
fetched_at: '2026-06-28T22:41:33.658156+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: CROSS Segmentos - Backoffice Protheus - TAF - REINF - Como gerar o evento R-4010
  ou R-4020 com dados de origem do Protheus?
type: support-article
updated_at: '2025-01-10T12:18:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16285623960727-CROSS-Segmentos-Backoffice-Protheus-TAF-REINF-Como-gerar-o-evento-R-4010-ou-R-4020-com-dados-de-origem-do-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16285614171671) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como gerar o evento **R-4010** ou **R-4020**, desde a origem das informações no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - **SIGATAF** - Todas as versões  
  
**Solução**

Os Eventos **R-4010** ou **R-4020** podem ser gerados a partir de notas fiscais que gerem financeiro ou de títulos incluídos diretamente no financeiro. Os Impostos que são considerados são: **IR**, sendo na emissão ou no pagamento(baixa do título) e o **PCC**, sendo considerado somente no pagamento(baixa do título). É obrigatório o vínculo da Natureza de Rendimento para que as informações sejam integradas corretamente ao TAF.

É obrigatório que toda a atualização de Backoffice, TAF e TSS esteja devidamente aplicada no ambiente para que as informações sejam geradas corretamente: [TAF - REINF - Atualização Completa Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-Reinf)

Exemplo de geração com origem em uma Nota Fiscal de entrada:

**1** - A nota fiscal precisa ter o cálculo da retenção de **PCC** e/ou **IR**: para o evento **R-4010**, somente **IR;** **R-4020, IR, PCC** ou ambos:

[MP - FIS - Retenção de PIS, COFINS e CSLL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056887693-MP-FIS-Reten%C3%A7%C3%A3o-de-PIS-COFINS-e-CSLL)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular o IRRF para notas de entrada e saída?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025517971-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-IRRF-para-notas-de-entrada-e-sa%C3%ADda)

Obs: No caso do evento **R-4010**, o fornecedor é Pessoa Física, já o **R-4020**, o fornecedor é Pessoa Jurídica. Para o cálculo do **IR**, caso o **IR** seja gerado na baixa, utilizar o campo **Cálculo IRRF = Baixa**no cadastro do Fornecedor; para dúvidas nessa etapa, avaliar junto ao time de **Escrita Fiscal.**

**2** - A nota precisa possuir um código de Natureza de Rendimento vinculado:

O vinculo da nota fiscal com a **Natureza de Rendimento** deve existir por meio da tabela **DHR**. Verificar o item 06 da documentação abaixo, que contém alguns facilitadores para o preenchimento desse código:

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - MATA103REINF - "Ocorrências" X "Soluções" no Doc Entrada x Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12498087063447-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-MATA103REINF-Ocorr%C3%AAncias-X-Solu%C3%A7%C3%B5es-no-Doc-Entrada-x-Reinf)

Caso ocorrer dúvidas nessa etapa, acionar o time **Protheus Compras.**

Caso ocorra alguma dúvida sobre qual código de Natureza de Rendimento utilizar, deve ser avaliado o anexo - **Tabelas** do Layout da ***Reinf*** 2.1.2 e utilizar um código que se adeque a operação que está sendo gerada: <http://sped.rfb.gov.br/pasta/show/7184>

**Observação**: A natureza de rendimento possui a coluna **TRIBUTO**, onde demonstra os impostos vinculados a aquele código. A operação, bem como quais retenções possui ou quando não há retenção, deve possuir um código que siga a mesma situação, **exemplo**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17972096715543)

O código **15049** não possui nenhum tributo, ou seja, trata-se de uma operação **sem retenção**. Já o código **15050** possui **IR e CSLL**. O **15048, Pis e Cofins**. Essa informação é de responsabilidade do cliente identificar qual código condiz com a operação que será transmitida ao ***Reinf***.

**3** - Efetuar a **baixa** dos títulos gerados no financeiro (exceto para **IR** na emissão, que será considerado da nota fiscal).

[Baixar títulos - SIGAFIN](https://tdn.totvs.com/display/public/PROT/Baixas+Pagar+Manual+-+FINA080+-+Financeiro+-+P12)

Caso ocorrer dúvidas nessa etapa, acionar o time **Protheus Financeiro.**

**4** - Executar o Extrator Fiscal, utilizando a pergunta Deseja Integrar = Ambos e Filtra ***Reinf*** = Sim.

Importante: Além dos layouts já utilizados atualmente para a ***Reinf***, o Layout responsável por levar os dados da baixa dos títulos dos impostos **PIS** e **COFINS** ou **IR** no pagamento ao TAF é o **layout T158.** A data a ser considerada das notas fiscais no extrator é sempre a data de entrada da nota e para a baixa dos títulos, é a data da baixa. **Se o T158 não for gerado ou não for integrado, o Painel Reinf não irá demonstrar os valores de PCC, somente IR.**

Caso o layout **T158** não esteja sendo gerado pelo extrator fiscal, acionar o time **Protheus Financeiro.**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como gerar o layout T158 REINF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16095149270423-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-gerar-o-layout-T158-REINF)

**5** - Efetuar o processamento pela rotina **Processamentos** (**TAFAINTEG**).

Acessar o **SIGATAF**, menu Miscelânea > Integração > Processamentos.

**6** - Verificar o **Gerenciador de Integração** se os dados foram integrados corretamente.

**Etapa obrigatória, pois os dados podem ser gerados pelo extrator, porém se ocorrer erros, as informações não serão levadas ao TAF.**

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como consultar o gerenciador de integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043361753-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-consultar-o-gerenciador-de-integra%C3%A7%C3%A3o)

No Painel ***Reinf***, os cards dos eventos do **bloco 40** só irão ser exibidos caso o parâmetro **MV\_TAFVLRE esteja com o conteúdo 2\_01\_02**

**Observações importantes:**

A estrutura dos dados que são integrados ao TAF são:

**T013** - Documento Fiscal

**T154** - Título do Financeiro (que pode ter vínculo com a nota fiscal ou ser um título avulso)

**T158** - Pagamento (*layout* que leva as informações da Baixa do título)

Caso seja integrado ao **TAF** uma nota fiscal com um título vinculado a essa nota, será exibido no Painel *Reinf* os dados com **origem somente no título**, com relação ao **IR** na emissão e contabilização.

Caso seja integrado somente a nota fiscal, será exibido no painel com base nessa nota, também somente do **IR** na emissão.

Caso seja integrado além dos layouts acima o **T158**, será exibido no **TAF** o **IR** da emissão (que pode vir ou do título ou da nota, caso a nota não possua duplicatas no financeiro) e o **Pis** e **Cofins** pelo pagamento ou o **IR** pelo pagamento.

**Apuração e Transmissão:**

Após o processo acima, os dados devem ser demonstrados no Painel *Reinf*.

No exemplo acima, caso a nota possua **IR** na Emissão e cálculo de **Pis** e **Cofins**, sendo que a emissão da nota foi 04/2023 e a baixa dos títulos de **PCC** foi 05/2023, o **IR** será demonstrado consultando o Painel *Reinf* pela data 04/2023 e os valores de **Pis** e **Cofins** serão demonstrados pela data 05/2023.

O Painel *Reinf* também conta com o **Relatório de Conferência**, onde é possível validar os registros antes da apuração dos mesmos. O relatório também segue a mesma lógica, pagamentos serão exibidos no mês da baixa e documentos do tipo fatura (vinculados ou não a uma nota fiscal) serão exibidos pela emissão.

É obrigatório que para a transmissão em produção, o **TSS** esteja com o acumulado de no mínimo 08/2024, caso contrário as transmissões poderão ocorrer rejeições diversas.

Para mais informações, consulte:

<https://tdn.totvs.com/display/public/TAF/EFD-Reinf>

<https://tdn.totvs.com/display/public/PROT/EFD-Reinf>
