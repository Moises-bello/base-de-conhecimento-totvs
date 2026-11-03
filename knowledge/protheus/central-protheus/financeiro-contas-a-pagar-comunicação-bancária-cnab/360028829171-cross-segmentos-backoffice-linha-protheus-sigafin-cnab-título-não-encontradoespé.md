---
article_id: 360028829171
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: f8afccedf9dc969126b763e1c6fda29fa41f702c834d38b7de420ae9e36628dd
fetched_at: '2026-06-28T22:37:55.364945+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Título não encontrado/Espécie
  não encontrada
type: support-article
updated_at: '2026-03-23T21:51:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028829171-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-T%C3%ADtulo-n%C3%A3o-encontrado-Esp%C3%A9cie-n%C3%A3o-encontrada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19838732606743)**Tempo aproximado para leitura: **00:05:00min**  
  
**Ocorrência**  
No módulo **Financeiro**, no processamento do **Retorno de Cobrança** (FINA200) e **Retorno de Pagamento**(FINA430) os títulos não são baixados, devido no Relatório de **Retorno Cnab** (FINR650), apresentar a consistência: "**Título Não Encontrado**". **Help NOESPECIE**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19838685393175)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois no retorno não é encontrado a chave de identificação do título que é o **IDCNAB**.

Ao gerar a remessa do arquivo de pagamento/cobrança é preenchido a numeração do **IDCNAB** com 10 caracteres no campo: **E1\_IDCNAB/E2\_IDCNAB**. No momento do **Retorno de Cobrança**(FINA200) e **Retorno de Pagamento**(FINA430) é feito análise nas tabelas **SE1**/**SE2** buscando o registro com a numeração dos campos **E1\_IDCNAB**/**E2\_IDCNAB** correspondente a numeração da posição**Seu Número** ou **Número do título**no arquivo de retorno. Como não foi localizado é apresentado: **Título não encontrado**. O **Nosso Número** é uma outra posição e através dessa numeração o banco valida os títulos e esse numeração é gravada no campo **E1\_NUMBCO**.  
A posição **Seu Número** (**IDCNAB**)é uma numeração de identificação do Protheus onde o banco não valida essa numeração.  
  
**Solução**  
Para solucionarmos o arquivo de configuração de retorno é ajuste a posição: **Seu Número** para buscar corretamente a numeração do **IDCNAB**, onde essa numeração é o próprio número gerado na remessa que foi gravado no campo: **E1\_IDCNAB**/**E2\_IDCNAB**.

**IMPORTANTE**

O Protheus considera 10 posições no IDCNAB, apesar do banco receber até 20 posições.   
Se o IDCNAB for configurado de 11 a 20 poderá ocasionar esse retorno.  
  
Por padrão do Protheus, a busca do **IDCNAB** começa da **Esquerda** para a **Direita** nas posições do retorno

**Exemplo abaixo:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19839171121175)**

**Outro ponto:**

Conforme demonstrado em vídeo *How To* (release 12.1.33), o campo **SUB CONTA** no cadastro de Parâmetros de Bancos (FINA130) é **obrigatório por padrão**.

A ausência de obrigatoriedade ou inconsistências no campo indicam **alterações fora do padrão (dicionário ou dados)**, podendo gerar comportamentos não previstos pelo sistema.

Ressalta-se que, via **SIGACFG**, não é possível remover essa obrigatoriedade no padrão, sendo essencial garantir o correto preenchimento do campo para evitar impactos nas rotinas financeiras.

[Principais Cadastros - CNAB](https://www.youtube.com/watch?v=f94kMIIDlcg)
