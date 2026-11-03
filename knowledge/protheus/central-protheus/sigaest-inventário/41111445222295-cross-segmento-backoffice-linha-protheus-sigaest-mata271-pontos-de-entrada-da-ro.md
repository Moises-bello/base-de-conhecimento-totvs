---
article_id: 41111445222295
category: SIGAEST - INVENTÁRIO
content_hash: 447e3f90ed9b08fcf4ac853e71aee797a5dc820ce7a59283a2c9c709b5ef2292
fetched_at: '2026-06-28T22:38:50.358234+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA271 - Pontos de
  Entrada da rotina Bloqueio de Inventário
type: support-article
updated_at: '2026-06-17T21:44:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41111445222295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA271-Pontos-de-Entrada-da-rotina-Bloqueio-de-Invent%C3%A1rio
---

O artigo detalha os Pontos de Entrada da rotina Bloqueio de Inventário (MATA271) no TOTVS Protheus. O MT271FIL permite aplicar filtros personalizados durante a leitura dos produtos, enquanto o MT271GRV possibilita executar rotinas customizadas no momento da gravação dos dados no banco, ao bloquear ou desbloquear itens para inventário. Links para mais detalhes e artigos relacionados são fornecidos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41111445214103) Tempo aproximado para leitura: **00:01:13 min**  
  
**Dúvida**  
Quais são os Pontos de Entrada relacionados à rotina Bloqueio de Inventário (MATA271)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Abaixo serão listados os Pontos de Entrada presentes na rotina MATA271:

**1. MT271FIL**

Este ponto de entrada é validado na inicialização das variáveis da função de processamento principal e executado durante a varredura dos produtos.

* **Localização no Código:** Está inserido dentro da função estática `A271Proces`.

* **Momento de Execução:** É chamado dentro do laço de repetição (`While`) que lê os registros de produtos e estoques retornados pela consulta ao banco de dados.
* **Parâmetro Enviado:** Ele recebe um array contendo a variável `mv_par01`, que indica se a operação atual é de Bloqueio ou Desbloqueio do inventário.
* **Finalidade:** Permite ao desenvolvedor aplicar um filtro customizado para cada produto posicionado. Caso o ponto de entrada retorne o valor lógico falso (`.F.`), o produto em questão é desconsiderado do processamento e o sistema salta para o próximo registro (`Loop`).

Link dos detalhes do Ponto de Entrada: <https://tdn.totvs.com/display/public/PROT/MT271FIL+-+Filtra+os+produtos>

**2. MT271GRV**

Este ponto de entrada está relacionado ao momento da persistência (gravação) dos dados no banco de dados.

* **Localização no Código:** Está inserido dentro da função estática `A271Grava`.
* **Momento de Execução:** É chamado dentro do laço de gravação da tabela temporária de trabalho (`TRB`), logo após o sistema atualizar e destravar os campos de data de inventário (`B2_DTINV` e `B2_DINVFIM`) na tabela de Saldos em Estoque (`SB2`).
* **Parâmetro Enviado:** Não recebe parâmetros adicionais por padrão (`.F., .F.`).
* **Finalidade:** Permite executar rotinas customizadas ou gravações complementares em tabelas personalizadas no exato momento em que cada item é bloqueado ou desbloqueado para o inventário.

Link dos detalhes do Ponto de Entrada: <https://tdn.totvs.com/display/public/PROT/MT271GRV>

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Inventário no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)
