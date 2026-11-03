---
article_id: 360026466213
category: GPE - eSocial - Não Periódicos
content_hash: e33db2cb4c5404439b2ef72aadaf7c20182f898bcc82487b3a24ca31764db196
fetched_at: '2026-06-28T22:45:04.396855+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200- Como calcular Rescisão para Estagiário
  através da rotina de Rescisão do SIGAGPE
type: support-article
updated_at: '2026-06-16T10:51:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026466213-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-calcular-Rescis%C3%A3o-para-Estagi%C3%A1rio-atrav%C3%A9s-da-rotina-de-Rescis%C3%A3o-do-SIGAGPE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27284625843607) Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Como calcular Rescisão para Estagiário através da rotina de Rescisão do SIGAGPE?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões   
  
**Solução**É possível utilizar a rotina de **cálculo de Rescisão do GPE (GPEM040)** para calcular a rescisão de estagiários (categoria 901 no eSocial).  
  
O **Protheus** não possui um tratamento padrão para a execução do cálculo da rescisão de estágio, uma vez que tal não possui vínculo empregatício e embasamento jurídico. Sendo assim, este documento demonstra a possibilidade do cliente executar o procedimento para atender a sua necessidade.

Salientamos também que estagiário não possui incidência em suas verbas, portanto, a Totvs não se responsabilizará pela geração de verbas incorretas no cálculo da rescisão.  
  
Para realizar o cálculo da rescisão de um Estagiário, favor seguir os seguintes passos:  
  
**Passo 1.**   
Cadastrar as verbas com Id de cálculo 1424, 1425, 0891 e 0219 (Caminho: SIGAGPE> Atualizações> Definições de cálculo> Verbas);**Passo 2.**   
Cadastrar o Tipo de Rescisão na tabela S043 (Caminho: SIGAGPE> Atualizações> Definições de cálculo> Manutenção de Tabelas);  
 **Passo 3.**   
Conferir se tem o período de recesso cadastrado no Controle Dias de Direito (Caminho: SIGAGPE> Atualizações> Funcionários> Controle Dias de Direito); **Passo 4.**   
Calcular a Rescisão (Caminho: SIGAGPE> Miscelânea> Cálculos> Rescisão); **Passo 5.**   
Ao gravar a Rescisão o evento **S-2399 será integrado com o TAF**, porém o evento S-2399 irá integrar apenas o cabeçalho da Rescisão:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27284625844759)  
 **Passo 6.**   
Integrar o **roteiro RES e calcular a Folha de Pagamento** para o Estagiário;  
 **Passo 7.**   
Acessar a rotina **Eventos Periódicos e integrar o evento S-1200** para o Estagiário, pois as verbas rescisórias serão declaradas no S-1200 e não no S-2399. Abaixo a imagem do XML S-1200 com as verbas rescisórias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27284625847319)  
  
De acordo com o [MOS S-1.2, no evento S-2399 (Trabalhador Sem Vínculo de Emprego/Estatutário - Término)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-052023.pdf), a informação relativa às verbas rescisórias devidas deve ser prestada, neste evento, no grupo [verbasResc] **apenas em relação aos diretores não empregados com FGTS - categoria [721].** Nos demais casos, **as verbas rescisórias devidas devem ser informadas nos eventos S-1200 ou S-1202,conforme o regime previdenciário do trabalhador.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27284670039959)**Rescisão - Integração do S-2399  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27284625854231)  
  
Eventos Periódicos - Integração S-1200  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27284670047127)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27284625861655)

**Saiba mais:**Para adquirir mais conhecimento acesse os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Para conhecimento dos eventos futuros, acessa a nossa página ***[TOTVS Informa](https://informa.totvs.com/)*** selecione em categorias a área e pesquise por "**Eventos**".
