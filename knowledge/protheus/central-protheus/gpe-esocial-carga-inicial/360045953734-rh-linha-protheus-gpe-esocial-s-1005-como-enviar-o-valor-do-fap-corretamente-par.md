---
article_id: 360045953734
category: GPE - eSocial - Carga Inicial
content_hash: 3245cb8eb45b379f8b73b6723efa436b2fe066815a4d0b65bf15b206e4f9983d
fetched_at: '2026-06-28T22:45:03.183245+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1005 - Como enviar o valor do FAP corretamente
  para o eSocial
type: support-article
updated_at: '2023-09-28T20:45:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045953734-RH-Linha-Protheus-GPE-eSocial-S-1005-Como-enviar-o-valor-do-FAP-corretamente-para-o-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17857325653399) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como enviar o valor do FAP corretamente para o eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**A partir da versão do Leiaute S-1.0, essa informação não é mais enviada ao eSocial, com exceção das regras destacadas abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17887616354327)  
  
O governo valida o valor do FAP diretamente no *site* <https://fap.dataprev.gov.br/>, então as informações acima são somente para o GPE calcular a folha. Por isso, é importante que não haja divergência entre as informações contidas no Protheus e eSocial.  
  
No módulo **SIGAGPE** acesse a rotina **Manutenção Tabelas**, porém não temos um campo para incluir essa informação diretamente, portanto devemos informar corretamente as informações nos campos **%Acid.Trab** e **%Rat** para que o sistema realize o cálculo do FAP na folha de pagamento.  
Caminho: *Atualização > Definições Cálculo > Manutenção Tabelas > Tabela S037 > Outras Ações > Alterar*:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17856799951511)  
  
Para calcular o valor do FAP, o sistema divide o **%Acid.Trab.** pela **%Rat**. Em nosso exemplo, o resultado seria 1,1686, estando esse valor dentro da validação demonstrada no Leiaute do eSocial na imagem anterior, não terá problemas de validação de valores.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17856909285399)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17857051845655)  
  
Para o TAF, os campos **FAP** e **Proc. FAP** estarão vazios e devem ser preenchidos manualmente e enviados para o eSocial **somente** nas condições descritas abaixo:   
- [ideEstab/tpInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#1005_infoEstab_inclusao_ideEstab_tpInsc) = [4] e o campo [cnpjResp](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#1005_infoEstab_inclusao_dadosEstab_cnpjResp) não estiver informado; ou  
- [ideEstab/tpInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#1005_infoEstab_inclusao_ideEstab_tpInsc) = [1, 4] e o fator informado for diferente do definido pelo órgão governamental competente para o estabelecimento ou para o CNPJ responsável pela inscrição no CNO (neste caso, deverá haver informações de processo em [procAdmJudFap](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#1005_infoEstab_inclusao_dadosEstab_aliqGilrat_procAdmJudFap)); ou  
- [ideEstab/tpInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#1005_infoEstab_inclusao_ideEstab_tpInsc) = [1, 4] e o estabelecimento ou o CNPJ responsável pela inscrição no CNO não for encontrado na tabela FAP.  
Ou seja, caso não exista a informação no <https://fap.dataprev.gov.br/> ou caso exista um processo administrativo a informação deverá ser incluída no TAF  
Para isso, acesse o caminho: *SIGATAF > Atualizações > Eventos eSocial > Tabelas > Estab, Obras Ou Unid. Órg. Públicos*: *![](https://centraldeatendimento.totvs.com/hc/article_attachments/17857169524887)*  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17872873515927)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[FAP 2024](https://www.totvs.com/blog/fiscal-clientes/fap-2024-novo-portal-de-consulta-e-contestacao/)  
[Artigos S-1005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822873)[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
