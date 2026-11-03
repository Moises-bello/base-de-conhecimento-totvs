---
article_id: 4413322763543
category: RH - Definições de Cálculo
content_hash: 14ac49cf26e7c20c84866d297a4569b5df99875779f44c32026aac65eb35ef17
fetched_at: '2026-06-28T22:43:22.503022+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Parecer SEI Nº 16120/2020/ME - Pagamento de adicionais
  legais (Novos Identificadores de cálculo ID 1873, ID 1874, ID 1875, ID 1876 e ID
  1877)
type: support-article
updated_at: '2025-09-30T17:43:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413322763543-RH-Linha-Protheus-GPE-Parecer-SEI-N%C2%BA-16120-2020-ME-Pagamento-de-adicionais-legais-Novos-Identificadores-de-c%C3%A1lculo-ID-1873-ID-1874-ID-1875-ID-1876-e-ID-1877
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337915159831)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Adaptar o sistema de acordo com o Parecer SEI Nº 16120/2020/ME e seu reflexo na contribuição patronal e no desconto do INSS do segurado. (Novos Identificadores de cálculo ID 1873, ID 1874, ID 1875, ID 1876 e ID 1877)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No site do eSocial [disponivel neste link,](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-) o governo detalhou o tratamento que deve ser realizado, [verifique o Boletim Técnico.](https://tdn.totvs.com/pages/viewpage.action?pageId=644726179)  
O tratamento já existente e [documentado](https://tdn.totvs.com/pages/releaseview.action?pageId=583789833)deve ser estendido para o pagamento dos adicionais legais (Periculosidade, Insalubridade, Tempo de Serviço, Transferência e Confiança).

**Nota**O governo alterou a incidência do eSocial da rubrica que deve ser informada quando o afastamento ultrapassa 15 dias. Na orientação anterior, a incidência CP era **15** e agora a incidência CP passa a ser **00**.  
  
Para possibilitar que os adicionais referentes aos dias de afastamentos superiores a 15 dias não sejam utilizados como base dos encargos empresariais e da contribuição do funcionário, 5 novos identificadores de cálculo foram criados, e devem ser cadastrados sem incidência para INSS e com incidência CP = **00**as demais incidências podem permanecer iguais as verbas referente ao pagamento do adicional.  
  
**Os novos identificadores são os seguintes:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Descrição** | **Incidência INSS (RV\_INSS)** | **Incidência CP (RV\_INCCP)** | **Id. Cálculo** |
| Adic. Confiança sem incidências | N | 0 | 1877 |
| Adic. Tempo Serviço sem incidências | N | 0 | 1875 |
| Adic. Transferência sem incidências | N | 0 | 1876 |
| Insalubridade sem incidências | N | 0 | 1874 |
| Periculosidade sem incidências | N | 0 | 1873 |

  

Quando existir afastamento por doença superior a 15 dias, configurado para não gerar encargos ([RCM\_PDSUP](https://tdn.totvs.com/pages/viewpage.action?pageId=585672041)), o sistema irá separar a parte dos adicionais referentes aos dias trabalhados e aos dias de afastamento pagos pela empresa, conforme o exemplo abaixo:  
  
**Exemplo:** Considerando que o funcionário, em um mês normal, deveria receber 600,00 de um adicional qualquer, caso ele esteja afastado por 16 dias no mês, o sistema irá gerar as verbas da seguinte forma:

|  |  |  |
| --- | --- | --- |
| **Adicional completo** | **Verba com incidência** | **Verba sem incidência** |
| 600 | 600,00 / 30 \* 14 => 280,00 | 600,00 / 30 \* 15 => 300,00 |

**Saiba Mais**  
[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[Parecer SEI Nº 16120/2020/ME - Incidências nos 15 primeiros dias de afastamento](https://tdn.totvs.com/pages/releaseview.action?pageId=583789833)  
[Parecer SEI Nº 16120/2020/ME - Alteração no cálculo da contribuição patronal e do desconto de INSS do segurado na folha](https://tdn.totvs.com/pages/viewpage.action?pageId=585672041)
