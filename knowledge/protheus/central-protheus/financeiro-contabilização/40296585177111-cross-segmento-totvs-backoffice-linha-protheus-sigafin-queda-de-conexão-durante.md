---
article_id: 40296585177111
category: Financeiro - Contabilização
content_hash: ef5b9271b5b0750a53c07eadda13c98dbe0fbac39c16fdb9913b813a0e3dc9e5
fetched_at: '2026-06-28T22:38:05.292856+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Queda de conexão
  durante contabilização não grava os dados na CT2 e mantem o Flag = S
type: support-article
updated_at: '2026-05-08T11:19:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40296585177111-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Queda-de-conex%C3%A3o-durante-contabiliza%C3%A7%C3%A3o-n%C3%A3o-grava-os-dados-na-CT2-e-mantem-o-Flag-S
---

**Dúvida**  
Quando ocorre a interrupção da contabilização de um título financeiro (exemplo: interrupção por queda de conexão), o sistema grava o campo E5\_LA marcado como 'S', porém sem a devida gravação dos lançamentos na tabela de Contabilidade (CT2), impedindo a recontabilização.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**  
O registro no Financeiro somente fica disponível para nova contabilização quando o campo de flag (E5\_LA) possui o conteúdo "N" ou "Vazio/Nulo". Se o conteúdo for "S", o sistema entende que o título já foi processado, impossibilitando a recontabilização automática.

Por padrão, o fluxo de preenchimento da flag ocorre no momento em que o sistema aciona o Lançamento Padrão (LP). Isso significa que, dependendo da configuração, o título pode receber a marcação de contabilizado antes mesmo da gravação efetiva no CT2/CV3/CTK ou da confirmação da tela de lançamentos.

Para mitigar este risco e garantir que a flag seja gravada apenas após a confirmação do processo, pode-se utilizar o parâmetro **MV\_CTBFLAG**.

Configurações do parâmetro:

1. **MV\_CTBFLAG = F (Falso):** A flag é marcada pelo próprio módulo que executa a contabilização. Em determinados processos, isso ocorre antes da confirmação na tela de lançamentos contábeis. Se houver queda de conexão ou erro de sistema neste intervalo, o registro fica com "S" sem ter gerado o CT2.
2. **MV\_CTBFLAG = T (Verdadeiro):** A flag é marcada somente após a confirmação (gravação/salvamento) da tela de contabilização. Esta configuração é recomendada para manter a coerência entre o que foi confirmado pelo usuário, o que foi efetivamente gravado na contabilidade e a marcação do título.

**Importante:**

Esse parâmetro não interfere quando a validação do sistema retorna “falso”. Pois mesmo assim, o sistema ainda passa pelo processo de contabilização mesmo sem apresentar o registro em tela.

* Se a regra não for atendida, o sistema não mostra o registro para análise
* Mesmo assim, o campo de flag será preenchido com **“S”, pois analisou a condição da sintaxe inserida.**

Outro ponto importante:

* Se uma linha contabilizada for excluída, isso significa que o usuário optou por não seguir com a contabilização
* Ainda assim, o sistema também grava o flag como **“S”**, pois houve interação dentro do processo

Resumindo:  
O **“S” no flag não significa que foi contabilizado com sucesso**, apenas que o sistema passou por uma tentativa de processamento, e durante estas excessões o comportamento do MV\_CTBFLAG (que exige confirmação do usuário) não será impactado, respeitando o padrão do sistema.
