---
article_id: 23871426315799
category: eSocial - Gerar XML/ Integração Evento
content_hash: 90259da00ca531e1711e1bc21ec68c902ec6ff8b4d041642261041057c4caf4f
fetched_at: '2026-06-28T22:47:13.157160+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - S-2299 - Erro 241: Motivo do desligamento inválido.
  Ação Sugerida: O valor informado no campo deverá existir na Tabela 19 (Motivo do
  Desligamento) e ser compatível com o código de categoria do trabalhador definido
  na mesma'
type: support-article
updated_at: '2026-06-15T13:10:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23871426315799-RH-RM-FOP-eSocial-S-2299-Erro-241-Motivo-do-desligamento-inv%C3%A1lido-A%C3%A7%C3%A3o-Sugerida-O-valor-informado-no-campo-dever%C3%A1-existir-na-Tabela-19-Motivo-do-Desligamento-e-ser-compat%C3%ADvel-com-o-c%C3%B3digo-de-categoria-do-trabalhador-definido-na-mesma
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23871426287767) Tempo aproximado para leitura: **00:03:30 min**  
  
**Ocorrência**  
Ao enviar o evento S-2299, o governo retorna o Erro código 241: Motivo do desligamento inválido. Ação Sugerida: O valor informado no campo deverá existir na Tabela 19 (Motivo do Desligamento) e ser compatível com o código de categoria do trabalhador definido na mesma.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23871465623703)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O erro ocorre quando no XML S-2299 é gerado um motivo de desligamento que não é compatível com a categoria do trabalhador, conforme informações do Leiaute de Tabelas.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Identifique no XML S-2299 o motivo de desligamento;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23871426291735)

2. Acesse o portal do governo, acesse **Empregado| Gestão de Empregados** digite o CPF do funcionário e identifique no seu cadastro a **Categoria eSocial**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23871465629847)

3. Valide na [**Tabela 19 do Leiaute de Tabelas**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s-1-3-cons-nt-05-2025/tabelas.html#19) se o motivo de desligamento é compatível com a categoria;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23871426294679)

4. No exemplo acima, o motivo 39 só será aceito para as categorias 301, 306 e 309, sendo necessário ajustar o motivo de desligamento na rescisão, visto que este motivo não é aceito para a categoria 101.

4.1 Para correção, acesse a **Rescisão - Aviso Prévio**e informe o Tipo de Demissão desejada;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23871426296343)

4.2. Caso o Motivo de Desligamento não conste no [**Mapeamento do Sistema**](https://tdn.totvs.com/display/public/LRM/Evento+S-2299)**,**será necessário realizar o [**De/Para Desligamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21705885729431-RH-RM-FOP-eSocial-S-2299-Motivo-desligamento-eSocial).

5. Regere o XML S-2299 e integre com o governo.
