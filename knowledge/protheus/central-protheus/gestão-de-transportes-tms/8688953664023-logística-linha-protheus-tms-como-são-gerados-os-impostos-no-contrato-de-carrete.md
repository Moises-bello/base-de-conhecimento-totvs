---
article_id: 8688953664023
category: Gestão de Transportes (TMS)
content_hash: a51eec1af48c60315f8b2df67902fe62d1e0a5b8f0c9bc19a2f6213445fee9af
fetched_at: '2026-06-28T22:45:27.500509+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como são gerados os impostos no Contrato
  de Carreteiro
type: support-article
updated_at: '2025-12-23T17:20:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8688953664023-Log%C3%ADstica-Linha-Protheus-TMS-Como-s%C3%A3o-gerados-os-impostos-no-Contrato-de-Carreteiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15243892625559) Tempo aproximado para leitura: **00:06:55 min**  
  
**Dúvida**  
Quais impostos incidem sobre o **Contrato de Carreteiro** no **SIGATMS** e como são calculados?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Os impostos no **Contrato de Carreteiro - TMSA250** são gerados da seguinte forma:

* **INSS - Instituto Nacional do Seguro** **Social**:  
  Instituído por legislação federal, sendo transporte de cargas, esse tributo terá a base de calculo de 20% sobre o valor do frete carreteiro, sobre o qual devera ser feita a retenção - desconto de 11% para posterior recolhimento - pagamento ao fisco. Cabe salientar que o desconto não pode ultrapassar o teto mensal estabelecido pela legislação, conforme cita a **Lei 10.666/2003**.  
    
  Para calcular o **INSS**, se no cadastro de **Fornecedor** - **MATA020** do proprietário do veiculo, o campo **Calc. INSS - A2\_RECINSS** estiver como **S - Sim**, o valor do **INSS** será calculado automaticamente pelo modulo **Financeiro**.   
    
  Para o calculo **INSS - DTY\_INSS**, o Sistema aplica a base de **INSS** informada no cadastro de **Naturezas - FINA010** do Contrato de Carreteiro, sob o Valor do Frete - **DTY\_VALFRE** do Contrato de Carreteiro que está sendo gerado. Depois aplica neste valor, o percentual de **INSS**.  
    
  Para que o Contrato de Carreteiro retenha o **INSS**, é necessário cadastro na rotina do modulo **Financeiro - Cadastro de Retenções Prévias - FINA027.**
* **SEST - SERVIÇO SOCIAL DO TRANSPORTE - SENAT - SERVIÇO NACIONAL DE APRENDIZAGEM DO TRANSPORTE:**  
  Regido por legislação federal, este valor deverá ser retido quando a prestação de serviços de transporte for realizada por **TAC - Transportador Autônomo de Carga**. A base de calculo do **SEST/SENAT** é composta de 20% sobre o valor do frete a ser pago ao terceiro.  
    
  O calculo do **SEST/SENAT** ocorrerá se no cadastro de Fornecedor do proprietário do veiculo, o campo **Recolhe SEST - A2\_RECSEST** estiver como **1 - Sim**, então, será gerado automaticamente pelo **Financeiro** um titulo a pagar, registro **SE2**.  
    
  Para o calculo do **SEST/SENAT - DTY\_SEST,** o Sistema aplica a base de **SEST** informada no cadastro de **Naturezas - FINA010** do Contrato de Carreteiro, sob o Valor do Frete do Contrato de Carreteiro, que está sendo gerado. Depois aplica neste valor, o percentual de **SEST**.   
    
  Caso seja necessário arredondar ou truncar o valor do **SEST/SENAT** deve-se configurar o parâmetro **MV\_RNDSEST** - Informe o critério de arredondamento do **SEST/SENAT**. As opções validas são .T. Arredonda e .F. Trunca.
* **IRRF - IMPOSTO DE RENDA RETIDO NA FONTE:**  
  Baseado em legislação federal, é o valor do imposto de renda que deverá ser retido - descontado do valor a pagar ao terceiro, este tributo incidirá sobre o somatório de todos os fretes pagos ao terceiro - agregado dentro do mesmo mês, sendo a base de calculo de 10% sobre o valor do frete carreteiro.  
    
  Este imposto é calculado automaticamente no modulo **Financeiro** se:
  + Se a **Natureza - FINA010** estiver configurada para o calculo de imposto de renda e o proprietário do veiculo for do tipo Pessoa Física - **A2\_TIPO = F**, então, ao confirmar o Contrato de Carreteiro, o Sistema varrerá o arquivo - DTY do Contrato de Carreteiro, somando todos os valores de frete - **DTY\_VALFRE** e **IRRF** do fornecedor gerados no mês. Depois, soma o **Valor do Frete** do contrato que está sendo gerado com o Total do Frete no mês e passa este valor para a **Tabela de IR** para que seja encontrado o valor do **IR** do carreteiro. O Valor do campo de **IRRF - DTY\_IRRF** deste Contrato, será a subtração entre o Valor encontrado e o Total do **IRRF** no mês.
  + Se o proprietário do veiculo for Pessoa Jurídica **A2\_TIPO = J**, o Sistema aplicará no valor do Frete do contrato que está sendo gerado, o percentual de **IRRF**, informado no **Cadastro de Natureza** do **Contrato do Carreteiro**.

**Saiba mais**  
Para mais informações sobre os assuntos relacionados, acesse as documentações:  
[Logística - Linha Protheus - TMS - Cadastros básicos para geração de contrato carreteiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050319614-Log%C3%ADstica-Linha-Protheus-TMS-Cadastros-b%C3%A1sicos-para-gera%C3%A7%C3%A3o-de-contrato-carreteiro)  
[Logística - Linha Protheus - TMS - Principais parâmetros Contrato Carreteiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050187034-MP-TMS-Principais-par%C3%A2metros-Contrato-Carreteiro)  
[FIN0081\_CPAG\_Sest\_Senat\_Financeiro](https://tdn.totvs.com/display/public/PROT/FIN0081_CPAG_Sest_Senat_Financeiro)  
[RH - Linha Protheus - GPE - Como cadastrar ou atualizar a tabela de INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043059473-RH-Linha-Protheus-GPE-Como-cadastrar-ou-atualizar-a-tabela-de-INSS?source=search)  
[Cadastros para o calculo de IRRF Carreteiro](https://tdn.totvs.com/display/public/PROT/FIN0026_CPAG_Calculo_de_IRRF_+Carreteiro)  
[Cross Segmento - Backoffice Linha Protheus - Parâmetros para ajustes de Retenção de INSS no Módulo (06) FINANCEIRO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019175871-Cross-Segmento-Backoffice-Linha-Protheus-Par%C3%A2metros-para-ajustes-de-Reten%C3%A7%C3%A3o-de-INSS-no-M%C3%B3dulo-06-FINANCEIRO?source=search)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA027 - Cadastro Previa de INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021009912-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA027-Cadastro-Previa-de-INSS)  
[Logística - Linha Protheus - TMS - Contrato de Carreteiro Com Retenção INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9607092232599-Log%C3%ADstica-Linha-Protheus-TMS-Contrato-de-Carreteiro-Com-Reten%C3%A7%C3%A3o-INSS?source=search)  
[Exemplo de Utilização Contrato de Carreteiro Com Retenção INSS (TMSA250 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=714227582)  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Arredondamento de Impostos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023920652-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Arredondamento-de-Impostos)
