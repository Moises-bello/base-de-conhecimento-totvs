---
article_id: 7093805910807
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f77a9972e3172b0dd8835f17de1cfeeeefdd2e845f799d559e418d375e7508dc
fetched_at: '2026-06-28T22:38:55.593978+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP REGBLOQ Este
  registro está bloqueado para uso SA1-Clientes ao efetivar uma transferência entre
  filiais.
type: support-article
updated_at: '2022-06-29T14:53:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7093805910807-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-REGBLOQ-Este-registro-est%C3%A1-bloqueado-para-uso-SA1-Clientes-ao-efetivar-uma-transfer%C3%AAncia-entre-filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:35 min****Ocorrência**Ao realizar a efetivação da MATA311 (Transferência Entre Filiais) é apresentado o HELP REGBLOQ Este registro está bloqueado para uso SA1-CLientes  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Este Help normalmente é apresentado em cenários que a filial destino, já estava cadastrado como Cliente, mas por algum motivo houve a necessidade de bloqueio deste cadastro A1\_MSBLQL = 1 e a criação de um novo Cadastro de Cliente com o Mesmo CNPJ.  
  
**Solução**Neste cenário, por Padrão a MATA311 vai buscar o primeiro registro existente na tabela SA1 e vai retornar o Help:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7093188077719/mceclip0.png)  
Uma medida de contorno seria a utilização do parâmetro MV\_FILTRF, na qual você define qual filial pertence esse cadastro de cliente/Fornecedor, sendo assim ele puxa o cadastro correto!

Segue processo:  
1. Acesse o módulo configurador (SIGACFG);  
2. Acesse o caminho Ambiente - Cadastros - Parâmetros;  
3. Localize e configure o parâmetro MV\_FILTRF = T ;  
4. Acesse no módulo de compras a rotina Fornecedores (MATA020);  
5. Cadastre um fornecedor e preencha o campo Fil. Transf (A2\_FILTRF);  
6. Acesse no módulo de vendas a rotina Clientes (MATA030);  
7. Cadastre um cliente e preencha o campo Fil. Transf (A1\_FILTRF);

**Importante:** Os campos A1\_FILTRF e A2\_FILTRF devem ser preenchidos com a filial que é correspondente aquele Cadastro de Cliente/Fornecedor.

Após esse processo, basta realizar uma nova tentativa de efetivar a transferência.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
