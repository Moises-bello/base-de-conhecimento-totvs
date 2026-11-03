---
article_id: 34423570599959
category: GPE - eSocial - Periódicos
content_hash: 370d50b9e7dcd41b380cf4823116cf6b7c46d546d7a9dcad4dada60ddd479d21
fetched_at: '2026-06-28T22:45:07.515789+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial -  Nota Técnica S-1.3 Nº 04/2025 - Natureza
  de Rubrica X Incidência de INSS
type: support-article
updated_at: '2025-09-11T12:00:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34423570599959-RH-Linha-Protheus-GPE-eSocial-Nota-T%C3%A9cnica-S-1-3-N%C2%BA-04-2025-Natureza-de-Rubrica-X-Incid%C3%AAncia-de-INSS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34423594258071) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
A [Nota Técnica S-1.3 Nº 04/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-04-2025.pdf) traz algumas alterações que entram em vigor em 29/08/2025.  
  
Foi incluída uma nova regra para recepção dos eventos remuneratórios que depende exclusivamente da avaliação da Tabela de Verbas/Eventos.

A partir dessa data as verbas/eventos com incidência tributária para a Previdência Social (INSS), que estiverem como 15 – Exclusiva do segurado – Mensal OU 16 – Exclusiva do segurado – 13° salário, só serão aceitas se a Natureza de Rubrica permitir tal configuração.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Solução**  
Para realizar essa conferência é necessário avaliar a **tabela 03-Natureza de Rubrica**, do eSocial, que está na página oficial do eSocial <https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-04-2025/tabelas.html#03>

Nessa tabela foi criado o campo **{codIncCP} EM S-1010 = [15, 16]**, este campo estando como **SIM**, indica que a **incidência de INSS poderá ser exclusiva do empregado (códigos 15 ou 16)**

Caso tenha alguma verba com a incidência INSS eSocial com código 15 ou 16, e a Natureza de Rubrica indique que essa verba não é compatível com essa incidência, os eventos remuneratórios (S-2299, S-2399 e S-1200) que contenham essa verba, serão rejeitados pelo ambiente do Governo (RET), a partir de 29/08/2025.  
  
**Adequações no Protheus**  
Estamos adequando as rotinas do eSocial para que apresentem essa ocorrência em log, mas enquanto os pacotes não são liberados, orientamos que avaliem a sua tabela de verbas (SRV)  para que possam fazer as alterações necessárias antes do fechamento da folha.  
  
**Sugestão de analise:**  
1 - Acesse a tabela de Verbas, em **Atualizações\Definições de Cálculos\Verbas;**  
2 - Criar um filtro utilizando o campo **Cd.Inc.CP (RV\_INCCP);**  
3 - O filtro deverá ser  **Cd.Inc.CP igual a 15 OU Cd.Inc.CP igual a 16**  
4 - Aplicar o Filtro  
5 - Serão listadas todas as verbas com essa incidência  
6 - Verificar o campo **Natureza (RV\_NATUREZ)**  
7 - Na tabela do eSocial <https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-04-2025/tabelas.html#03>, verificar se o novo campo**{codIncCP} EM S-1010 = [15, 16] está igual a SIM**, para a Natureza da verba apresentada no filtro  
8 - Se estiver igual a **SIM não é necessário nenhuma ação**  
9 - Se estiver igual a **NÃO**, indica que, se a verba constar em algum evento remuneratório, a partir de 29/08/2025 esse evento será rejeitado pelo Governo, sendo assim deve ser avaliado o melhor caminho a ser tomado, consultando o Jurídico da empresa.  
  
  
**Saiba Mais**  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-04-2025.pdf)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
