---
article_id: 1500001580661
category: LEGAIS - BLOCO H/MATR460
content_hash: be1d02873b6d0900817d1702228bf2fb19afce8a2a87f05579c97466fb3adfa6
fetched_at: '2026-06-28T22:42:15.016725+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco H - Não está
  sendo gravado o Código do Participante na tabela H e Registro H010 (COD_PART)
type: support-article
updated_at: '2021-05-03T18:57:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001580661-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-H-N%C3%A3o-est%C3%A1-sendo-gravado-o-C%C3%B3digo-do-Participante-na-tabela-H-e-Registro-H010-COD-PART
---

**Dúvida**

Ao gerar o SPED Fiscal, no Registro H010 do Bloco H não está trazendo no COD\_PART o Código do Participante de alguns saldos de produtos. O que fazer?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**

Para solucionar este problema, siga os passos abaixo.

**1° Passo - Valide se a seu ambiente está atualizado**

Este problema pode estar relacionado com o ambiente estar atualizado ou não. Então, certifique-se de que os Acumulados de Estoque e Livros Fiscais estão atualizados:

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

***Pacotes acumulados Livros Fiscais:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/956585) **|**12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/805589) **|**12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/770598)

Após aplicar os acumulados, gere o MATR460 e SPED Fiscal para validação.

**2° Passo - Avaliação via tabela SB6 (B6\_TPCF)**

Avalie, via tabela SB6 (Saldo em Poder de Terceiros), o(s) movimento(s) de controle de Poder de Terceiros para o produto com o problema. No campo B6\_TPCF (Indica o Tipo, sendo Cliente ou Fornecedor), é necessário estar preenchido com F (Fornecedor) ou C (Cliente). Avalie também se não há registro deletado na APSU para o movimento ou se o registro está em branco

Se identificar campo em branco ou deletado, faça o ajuste para gerar o MATR460 e SPED novamente.

**3° Passo - Avaliação do Cliente/Fornecedor no Protheus e na base de dados**

Avalie a existência do Cliente/Fornecedor em questão nas tabelas SA1 (Cadastro de Clientes) e SA2 (Cadastro de Fornecedores). O mesmo pode estar bloqueado ou deletado na base de dados.

Se identificar cliente/fornecedor bloqueado ou deletado, faça o ajuste para gerar o MATR460 e SPED novamente.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H)*
