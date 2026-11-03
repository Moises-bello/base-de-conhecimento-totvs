---
content_hash: ae5d40a041ae574dd7e4263b5ba3eec816c59a6f196ac8deb45111c4ad30a889
fetched_at: '2026-06-29T00:12:14.237680+00:00'
page_id: '967107264'
product: rm
source: tdn-rm
title: DT - Lançamento Financeiro - Tipo "25 -Total Guia INSS DCTFWeb" e "26 -Total
  Guia INSS DCTFWeb 13° Salário" - Evolução no Log
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=967107264
version: 13
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Lançamento Financeiro - Tipo "25 -Total Guia INSS DCTFWeb" e "26 -Total Guia INSS DCTFWeb 13° Salário" - Evolução no Log |
| País: | Brasil |
| Épico | [DRHROTRM-12818](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12818) |

## **02. VERSÃO**

* 12.1.2502.180
* 12.1.2506.122 e superiores

## **03. S****ITUAÇÃO/REQUISITO**

Aperfeiçoamento do log do Lançamento Financeiro do tipo **"25 -Total Guia INSS DCTFWeb"** e **"26 -Total Guia INSS DCTFWeb 13° Salário"** , com o objetivo de proporcionar uma experiência ainda melhor para nossos clientes, oferecendo aos usuários mais autonomia na conferência e na identificação de possíveis inconsistências.

## **04. SOLUÇÃO**

O lançamento financeiro passou a contar com uma nova aba de debug que detalha os valores calculados para cada lançamento. Com essa melhoria, os usuários terão acesso a informações mais completas e maior visibilidade sobre os dados registrados, facilitando a identificação e correção de eventuais inconsistências.

Os valores apresentados na aba incluem: Empresa, Segurados, Acidente de Trabalho, Terceiros e Deduções

1true1Log Antes da EvoluçãoLog Antes da Evolução

Demonstração do Log do Lançamento Financeiro antes da inovação:

## Geração de Lançamentos Financeiros INSS DCTFWeb ##  
Lançamentos Financeiros gerados:  
------------------------------------------------------------------------------------------  
Lancto. Fin. ID: 9998145 ---> Tipo: [INSSPagar] Valor: 14.607,28

------------------------------------------------------------------------------------------  
Total de Lançamentos Financeiros efetuados: 1  
### Fim memória de Cálculo

true3Log Após a EvoluçãoLog Após a Evolução

Demonstração do Log do Lançamento Financeiro após a inovação:

IMPORTANTE:

* Os valores de terceiros serão detalhados somente quando o parâmetro **"Utiliza quebra de FPAS"** estiver desmarcado. Existente em **Configurações | Parametrizador |  eSocial |** **Lotação Tributária**.
* Além disso, quando houver utilização de tomador de serviço, poderá ocorrer diferença de centavos no lançamento. Nesse caso, o log apresentará uma linha informativa com o ajuste realizado no lançamento financeiro, identificada pela descrição **"Total Lanc Financ Ajustado"**.
3Dicas para a geração corretaDicas para a geração correta

Para garantir a geração bem-sucedida do lançamento financeiro, é essencial verificar as configurações do Parametrizador, das seções, parametrizações dos lançamentos financeiros, dentre outros.

Veja os detalhes em nosso link

## **05. DEMAIS INFORMAÇÕES**

[Cadastros Financeiros](https://tdn.totvs.com.br/display/public/LRM/Cadastros+Financeiros)
