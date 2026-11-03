---
article_id: 32409247102999
category: eSocial - Gerar XML/ Integração Evento
content_hash: dfbddaea80dce60944d9c8538b527f35545f79ea57a9ee3da20861ead6aa57e1
fetched_at: '2026-06-28T22:47:13.102017+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Parâmetro para Gerar Informações do Local de Trabalho
  nos Eventos S-2200, S-2206, S-2300 e S-2306
type: support-article
updated_at: '2026-06-05T17:06:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32409247102999-RH-RM-FOP-eSocial-Par%C3%A2metro-para-Gerar-Informa%C3%A7%C3%B5es-do-Local-de-Trabalho-nos-Eventos-S-2200-S-2206-S-2300-e-S-2306
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32409263647895) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Houve uma melhoria no produto  que permite, durante a geração dos eventos S-2200, S-2206, S-2300 e S-2306, definir se o grupo "Informações do local de trabalho" tag <localTrabGeral> será preenchido com os dados do CEI da obra própria ou com as informações da seção onde o funcionário está alocado. A opção é aplicada quando o colaborador está vinculado a um único tomador de serviço, proporcionando mais flexibilidade no envio das informações ao eSocial e melhor aderência aos diferentes cenários de alocação utilizados pelas empresas.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir da versão: 12.1.2406 e superiores  
  
**Solução**  
Para gerar os arquivos com essa informação, realize os seguintes passos:

1. Acesse **Configurações | Parametrizador | eSocial | Configurações Gerais 3/7** e habilite o parâmetro**;**

![image-2025-4-16_17-3-3.png](https://tdn.totvs.com/download/attachments/934636669/image-2025-4-16_17-3-3.png?version=1&modificationDate=1744833783733&api=v2)

2. Ao habilitar este parâmetro, o sistema passará a considerar os dados conforme o tomador de serviço informado no caminho: **Administração de Pessoal | Funcionário | Anexos | Históricos | Histórico de Rateio por Tomador;**

![https://tdn.totvs.com/download/attachments/927561882/image-2025-3-26_13-55-16.png?version=1&modificationDate=1743008117337&api=v2](https://tdn.totvs.com/download/attachments/927561882/image-2025-3-26_13-55-16.png?version=1&modificationDate=1743008117337&api=v2)

3. Arquivo **XML:**

![https://tdn.totvs.com/download/attachments/927561882/image-2025-3-26_14-2-3.png?version=1&modificationDate=1743008524043&api=v2](https://tdn.totvs.com/download/attachments/927561882/image-2025-3-26_14-2-3.png?version=1&modificationDate=1743008524043&api=v2)

Importante

Não será gerado gatilho na troca do tomador, ou seja, a alteração do tomador não dispara automaticamente o envio do evento S-2206 – Alteração de Contrato de Trabalho.

Somente com o parâmetro "Considera CNO nas tags localTrabGeral do S-1005 para funcionários alocados em um único tomador obra própria" marcado, o XML será gerado com as informações do CEI da obra própria no grupo "Informações do local de trabalho" (tag <localTrabalho>).

Saiba mais

[Mapeamento dos Eventos](https://tdn.totvs.com/display/public/LRM/Mapeamento+dos+Eventos)
