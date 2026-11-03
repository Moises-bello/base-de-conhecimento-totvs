---
article_id: 360020482651
category: LEGAIS - BLOCO H/MATR460
content_hash: d96967573138d36d3e259129aff1fa344b830d350c8233cbfa12878b2cec34c9
fetched_at: '2026-06-28T22:42:14.943722+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como parametrizar
  os relatórios MATR460 e MATR260 para comparação de divergência Saldo no Estoque?
type: support-article
updated_at: '2026-02-12T16:52:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020482651-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-parametrizar-os-relat%C3%B3rios-MATR460-e-MATR260-para-compara%C3%A7%C3%A3o-de-diverg%C3%AAncia-Saldo-no-Estoque
---

Para garantir que os relatórios MATR460 (Inventário Modelo 7 - P7) e MATR260 (Posição de Estoque) apresentem os mesmos saldos, é fundamental parametrizar ambos com os mesmos filtros e datas, além de alinhar configurações como saldo em processo, saldo em fabricação e parâmetros MV\_CUSFIL. Recomenda-se validar inicialmente apenas um produto para conferência.

**Dúvida**

Os valores apresentados no MATR460 (Inventário Modelo 7 - P7) são diferentes do MATR260 (Relatório Posição de Estoque). Como diagnosticar se parametrizei corretamente?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Normalmente ao final dos meses muitas empresas costumam, após o fechamento do estoque (virada de saldos), conferir como ficaram seus saldos daquele período, até mesmo para poder gerar arquivos fiscais como SPED, por exemplo, tendo a certeza de que o saldo que será gerado no arquivo estará correto. Com isso, o relatório MATR460 (P7) é utilizado com regularidade, mas em alguns momentos pode ser apresentado uma quantidade diferente do relatório MATR260 (Posição de Estoque). Então, como parametrizar estes relatórios para checar se realmente existe uma divergência entre os saldos nos relatórios?  
**Possuímos um vídeo, com todas as configurações necessárias e explicação sendo informadas:**

**Premissas a serem previamente validadas:**

* Certifique-se de que os campos "Produto De/Até", "Armazém De/Até", "Listar Produto Zerado?", estejam **100% iguais em ambos os relatórios (MATR260 e MATR460)**;
* A **data de referência/data de fechamento** devem ser **iguais** (é utilizada a mesma função **calcest()** para calculo de saldo do produto);
* A pergunta **"Saldo em Processo"** e **"Saldo em Fabricação"** devem estar configurados com o valor igual a **"NÃO"**, pois o relatório MATR260 não considera este tipo de saldo pois o mesmo já foi requisitado para produções e etc;
* Configurar a pergunta **"Saldo em poder 3º = NÃO"**;
* Se o parâmetro **MV\_CUSFIL = F** o relatório MATR260 deve ser configurado com a pergunta **"Aglutina por = FILIAL"**;
* Se o parâmetro **MV\_CUSFIL = E** o relatório MATR260 deve ser configurado com a pergunta **"Aglutina por = EMPRESA"**;
* MATR260 deve estar parametrizado com a pergunta **"Saldo do prod. a considerar? = por movimento"**para chamar a função calcest(), puxando assim os saldos conforme o MATR460 busca.

**Obs:**

A função calcest() está contida no fonte MATXFUNB, o mesmo possui a Stored Procedure 14 para melhoria de performance, caso esteja tendo problemas, faça um teste com esta Procedure desinstalada.

Com essas premissas cumpridas, o sistema fará as mesmas checagens para poder imprimir os mesmos saldos dos produtos tanto no relatório Posição de Estoque (MATR260) quanto o Registro de Inventário Modelo 7 (P7/MATR460).

**Sugerimos a validação APENAS DE 1 PRODUTO para verificação pontual.**

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)
