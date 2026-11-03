---
article_id: 360018286552
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 86a0a25c11f1b02d9d95b8a4e5d982c2ac1ce99b87fa79e4d3089594f46e86f0
fetched_at: '2026-06-28T22:39:07.839678+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como desabilitar customizações
  no Protheus?
type: support-article
updated_at: '2025-11-14T13:50:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-desabilitar-customiza%C3%A7%C3%B5es-no-Protheus
---

O artigo explica como desabilitar customizações no Protheus acessando o Catálogo de Personalização (CFGA030), alterando a situação da função para "Desabilitado", o que atualiza o campo X7\_STATUS para 2 na tabela XX7 e impede a execução da rotina. Outra opção é renomear o RPO custom e reiniciar os serviços para desativar todos os pontos de entrada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36335286089111) Tempo aproximado para leitura: **00:03:00min**

**Dúvida**

Como desabilitar Customizações pelo no Protheus?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

### **Via catalogo de personalização (CFGA030)**

devemos acessar a rotina catálogo de personalização (CFGA030). Então, no configurador, acesse:

**Ambiente -> Cadastros ->  Catálogo de Personalização** .

No nosso teste, temos uma função de usuário compilada no RPO custom e um menu personalizado criado para chamar a função ZCADORC. Devemos selecionar a função que queremos desabilitar e clicar em **Alterar** conforme imagem abaixo.

![CAT2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013892872)

Agora devemos expandir o campo “**Situação**” e escolher a opção “**Desabilitado**” conforme imagem abaixo.

![DES.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013908991)

**Ao executar esse procedimento, na tabela XX7 o campo X7\_STATUS deverá constar igual a 2**

E ao tentar executar a rotina será apresentada a mensagem de que a rotina não está compilada no RPO custom, conforme imagem abaixo.

![COMP.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013893032)

### **Via backup do rpo custom**

Voce tambem pode renomear o RPO custom, reinicar os serviços e acessar novamente, assim garante que todos os pontos de entrada seguem desativados para realizar teste sem pontos de entrada ativos.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
