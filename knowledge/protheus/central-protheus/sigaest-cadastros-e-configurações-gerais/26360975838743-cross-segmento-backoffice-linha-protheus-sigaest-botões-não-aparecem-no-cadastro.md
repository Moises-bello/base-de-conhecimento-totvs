---
article_id: 26360975838743
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 3e6e6dd1b588598a6d3259842038522efda36b84a519c1eb4e4a36f84bd4b156
fetched_at: '2026-06-28T22:39:08.052842+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Botões não aparecem
  no Cadastro de Produtos (MATA010)
type: support-article
updated_at: '2025-03-12T12:23:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26360975838743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bot%C3%B5es-n%C3%A3o-aparecem-no-Cadastro-de-Produtos-MATA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26360931263767) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao acessar a rotina de Cadastro de Produtos (MATA010) os botões "Incluir", "Alterar", "Visualizar" e "Excluir" não são apresentados  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Causa**Isso pode ocorrer caso o fonte padrão (MATA010.prw) tenha alguma interrupção em sua execução, essa interrupção pode ser causada por:

* Pontos de Entrada executados na abertura da tela de Cadastro de Produtos;
* Caso exista um fonte, customizado, compilado com o mesmo nome da rotina (MATA010.prw)

**Solução**Esses foram dois cenários que verificamos a ocorrência do incidente. Caso ocorra em seu ambiente, realize o seguinte processo:

1. Retire o ponto de entrada ou rotina customizada de seu RPO e realize um novo teste;

2. Os pontos de entrada ficam guardados no Custom.rpo ([RPO Custom](https://tdn.totvs.com/x/YElwJQ)):

* Em ambiente de Homologação, após os devidos Backups dos dados, é possível retirar o RPO Custom da pasta;
* Assim o sistema gera um RPO Custom novo e não executa as customizações, permitindo testar se elas estavam afetando a rotina padrão.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
