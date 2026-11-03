---
article_id: 38126303459735
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 38d294cbcb74a48c15a54b5be0c0b7a50f82775f4885094ed04ba3b54700a5d3
fetched_at: '2026-06-28T22:38:57.224332+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Nota de entrada nao
  movimentou estoque
type: support-article
updated_at: '2026-02-03T13:27:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38126303459735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Nota-de-entrada-nao-movimentou-estoque
---

A ausência de movimentação no estoque ou atualização no Kardex ao registrar uma nota de entrada no Protheus geralmente ocorre por parametrização incorreta da TES, especialmente se o campo "Atualiza Estoque" estiver como "N". Também é necessário revisar filtros do relatório e possíveis customizações que possam interferir no processo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38126303441303) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Efetuei uma "nota de entrada", mas validei que não foi gerado o movimento no estoque, ou atualizado no kardex, porque isso acontece?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Quando uma movimentação do documento de entrada não é apresentada no Kardex, a causa geralmente está relacionada à parametrização da TES. Siga o roteiro abaixo para identificar a origem do problema:

## **Validação da TES (Tipo de Entrada e Saída)**

O principal motivo para a ausência de registros no Kardex é o fato de a operação ser apenas financeira ou fiscal, sem impacto físico.

**Campo F4\_ESTOQUE:** Verifique se o campo Atualiza Estoque está configurado como "S" (Sim).

Se estiver como "N" (Não), o sistema não gerará movimentos nas tabelas de estoque (SD1) com impacto no saldo, e consequentemente, o item não constará no Kardex.

## **Filtros e Parametrização do Kardex**

Se a TES está correta, revise os parâmetros informados no momento da geração do relatório:

Armazém: Certifique-se de que o filtro contempla o armazém onde a nota foi lançada.

**Período (Data de/Até):** Verifique se a data de emissão ou de entrada do documento está dentro do intervalo selecionado.

## **Pontos de Entrada e Customizações**

Caso a TES atualize estoque e os filtros estejam corretos, mas o movimento persista em não aparecer:

Interferências: Valide se existem Pontos de Entrada que possam estar inibindo a gravação dos dados nas tabelas de estoque ou alterando o comportamento padrão do sistema.

Teste Padrão: Recomenda-se realizar um teste com as customizações desabilitadas para isolar o problema.

## **Próximos Passos para Atendimento**

Se após essas validações o problema persistir, por favor, encaminhe ao suporte os seguintes itens para uma análise detalhada:

**Vídeo de Evidência:** Grave o processo completo, demonstrando o cadastro da TES utilizada, a execução da movimentação e a ausência do dado no Kardex (preferencialmente com pontos de entrada desativados).

**ID da Central de Diagnóstico:** Envie o ID gerado para que possamos validar o nível de atualização do seu ambiente (RPO, Dicionário e Patchs), garantindo conformidade com o Portal do Cliente.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
