---
article_id: 38781985926167
category: SIGAEST - INTEGRAÇÕES
content_hash: 8ba29da6e418ab61750fb1132d3f2b2e2b2d1270c6e718f5f0ec1924e9625a86
fetched_at: '2026-06-28T22:38:46.168863+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração EAI: Carga
  Inicial'
type: support-article
updated_at: '2026-03-24T13:49:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38781985926167-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-EAI-Carga-Inicial
---

O EAI Protheus possui um sincronizador de carga inicial para integrar cadastros via EAI com outros sistemas, permitindo escolher adapters para iniciar a sincronização. O acesso é feito pelo Configurador (SIGACFG) em Ambiente Schedule Sinc.carga Inicial. Há uma interface para acompanhar o progresso via gráficos e logs. Mais informações estão na documentação oficial da TOTVS.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38781985915159) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como gerar a Carga Inicial dos dados para integração do Protheus com outros sistemas?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**  
O EAI Protheus possui um sincronizador de carga inicial para os cadastros  que podem ser trafegados via EAI. É possível, dentre os adapters cadastrados, escolher qual destes se deseja iniciar a sincronização, enviando todos os registros impactados por aquele adapter via EAI para o outro sistema.

Veja um vídeo sobre o processo:

[![Carga Inicial.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39256520851991)](https://youtu.be/MaT28_fFq7k?si=_V5897pwHNPkmBu9)

Para acessar o Sincronizador, basta conectar no Configurador do Sistema (**SIGACFG**), acessar a opção "Ambiente", depois "**Schedule**" e por fim a opção "**Sinc.carga Inicial**".

Selecionando a opção do sincronizador é apresentado o browse com todos os adapters já cadastrados no Protheus. Basta selecionar um adapter e clicar em Sincronização inicial.

 Existe uma interface própria para acompanhamento dos eventos enviados para sincronização. Esta tela permite através de gráficos e outras formas de visualização controlar o progresso da sincronização. Para acessar esta rotina, na tela de sincronização do EAI selecione em ações relacionadas/log de sincronização.

Para mais informações acesso a documentação completa em:

[**O Sincronizador de Carga Inicial do EAI Protheus**](https://tdn.totvs.com/x/CBAyCw)

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Integrações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
