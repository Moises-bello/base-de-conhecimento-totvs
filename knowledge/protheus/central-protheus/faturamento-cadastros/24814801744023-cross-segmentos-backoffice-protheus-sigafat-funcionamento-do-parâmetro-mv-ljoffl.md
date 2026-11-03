---
article_id: 24814801744023
category: Faturamento - Cadastros
content_hash: 3c5214e4df9cd0c1ceae82c7d03212eb40390309d98d597b1b6e5b2c04486614
fetched_at: '2026-06-28T22:38:35.457137+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Funcionamento do parâmetro
  MV_LJOFFLN no cadastro de clientes
type: support-article
updated_at: '2024-07-11T14:38:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24814801744023-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-LJOFFLN-no-cadastro-de-clientes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24814801691287) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o funcionamento do parâmetro MV\_LJOFFLN no cadastro de clientes?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**A ativação desse parâmetro (.T.) surtirá em duas funcionalidades no pedido de venda:

1 - Geração do código (A1\_COD) do cliente pelo CNPJ informado (A1\_CGC)

* Para saber a regra de constituição do código do cliente, orientamos que contate a Equipe Automação Comercial (SIGALOJA).

2 - Verificação entre todos os clientes já cadastrados, se existe algum com a mesma base do CNPJ.

* Por padrão, o faturamento possui o parâmetro MV\_VALCNPJ e MV\_VALCPF, para validarem o CNPJ e CPF completo, porém, o MV\_LJOFFLN avalia a base do CNPJ e avisa se existe algum com a mesma cadastrada, mesmo que os identificadores de filial e dígitos verificadores do outro CNPJ seja diferente:  
    
  CNPJ: XX.XXX.XXX/0001-ZZ (Verificado pelo MV\_VALCNPJ se existe algum outro completo igual)  
    
  Base: XX XXX XXX (Verificado pelo MV\_LJOFFLN se existe algum outro com base igual)  
  Identificadores de filial: 0001  
  Dígitos Verificadores: ZZ

**Saiba mais:**

* [Como desabilitar a geração do código de cliente a partir do CPF/CNPJ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235634028-Como-desabilitar-a-gera%C3%A7%C3%A3o-do-c%C3%B3digo-de-cliente-a-partir-do-CPF-CNPJ)
* [MP - SIGALOJA - Ao habilitar o parâmetro MV\_LJOFFLN esta sendo gerado o código de cliente duplicado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001647962-MP-SIGALOJA-Ao-habilitar-o-par%C3%A2metro-MV-LJOFFLN-esta-sendo-gerado-o-c%C3%B3digo-de-cliente-duplicado)
* [Cross Segmentos - Backoffice Protheus - SIGAFAT - Permitir/bloquear inclusão de clientes com CNPJ e CPF já informados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402371773975-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Permitir-bloquear-inclus%C3%A3o-de-clientes-com-CNPJ-e-CPF-j%C3%A1-informados)
