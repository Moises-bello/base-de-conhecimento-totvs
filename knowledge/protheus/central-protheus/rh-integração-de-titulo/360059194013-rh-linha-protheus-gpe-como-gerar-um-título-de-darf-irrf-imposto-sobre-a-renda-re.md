---
article_id: 360059194013
category: RH - Integração de Titulo
content_hash: aebe8f5af0bb3c70693c76bb88fe78275a6c1202a02718914407e6b537f6a8c1
fetched_at: '2026-06-28T22:43:36.239404+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar um título de DARF IRRF - Imposto sobre
  a renda retido na fonte
type: support-article
updated_at: '2025-07-24T20:32:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059194013-RH-Linha-Protheus-GPE-Como-gerar-um-t%C3%ADtulo-de-DARF-IRRF-Imposto-sobre-a-renda-retido-na-fonte
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33688164430103)** Tempo aproximado para leitura: 00:02:00 min

**Dúvida**  
Como gerar um título de DARF IRRF - Imposto sobre a renda retido na fonte?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Realize o cálculo do Roteiro FOL:  
![Roteiro_FOL.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/33688164432023)

2. Acesse Miscelânea -> Títulos -> Definição e configure um título de DARF IRRF. No exemplo abaixo usaremos uma definição padrão existente Imposto de Renda, mas pode ser usada a opção Definido pelo Usuário.   
![defini__o_irrf.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360097213734)

**Atenção:** Optando pela definição padrão, você poderá seguir para o ponto 4.  
  
  
3. Optando por Definido pelo Usuário, será apresentada uma janela para selecionarmos a verba e a tabela onde buscaremos o cálculo para geração do título. **Tratando-se de verbas da folha de pagamento, o cálculo estará na tabela SRC, estando o respectivo mês com período fechado os dados devem ser buscados na SRD**e utilizaremos como filtro para busca a Data de Pagamento:   
**![definido_pelo_usu_rio_INSS.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/33688115496855)**

**Atenção:** A legenda da  verba selecionada para geração deverá ser verde para que seja considerada na geração. Legendas vermelhas são consideradas como dedução do valor.    
  
4. Acesse Miscelânea ->Títulos -> Geração e configure os parâmetros de acordo com o título que será gerado:  
![geracao_titulos.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360099518093)  
  
  
5. Acesse Miscelânea -> Títulos -> Manutenção e verifique as informações do título gerado.   
![titulo_IRRF.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360097213654)

6. Acesse Relatórios -> Periódicos -> Dirf Mensal/Darf -> Darf o valor do título deve ser um reflexo da guia gerada nesta rotina:

![DARF_-_IRRF.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360097213694)

**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
