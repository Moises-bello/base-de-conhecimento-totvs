---
content_hash: c098cf607eca98fb097cf707cc80bc676e440131fdad7dcf8217d03c17a3bbf6
fetched_at: '2026-06-29T00:05:47.401908+00:00'
page_id: '1012939706'
product: rm
source: tdn-rm
title: Sped Fiscal - Alterações NFCom
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1012939706
version: 21
---

# Conteúdo

# Conteúdononenone

# Sobre

Com a publicação do Ajuste SINIEF nº 7, de 7 de abril de 2022, foi instituída a Nota Fiscal Fatura de Serviços de Comunicação Eletrônica (NFCom), modelo 62, com obrigatoriedade de uso a partir de 1º de Abril de 2025. Este ajuste substitui as Notas Fiscais de Serviço de Comunicação (modelo 21) e de Serviço de Telecomunicação (modelo 22).

# Versões para atualização

A solução está disponível a partir dos patches:

Data:  

Biblioteca RM

* 12.1.2502.248
* 12.1.2506.202
* 12.1.2510.132

# Alterações

## EFD ICMS IPI

Na geração da EFD ICMS IPI foram criados os seguintes registros:

### Registro D700 - Nota Fiscal Fatura Eletrônica de Serviços de Comunicação – NFCom (Código 62)

Este registro tem por objetivo escriturar notas de comunicação individualizadas, de entradas e saídas.

Documento auxiliar:

### Registro D730 - Registro analítico Nota Fiscal Fatura Eletrônica de Serviços de Comunicação – NFCom (Código 62)

Este registro tem por objetivo representar a escrituração dos documentos fiscais informados no registro D700 totalizados pela combinação de CST, CFOP e Alíquota de ICMS.

Documento auxiliar:

### Registro D731 - Informações do fundo de combate à pobreza – FCP – (Código 62)

Este registro tem o objetivo de gerar os valores de FECP próprio dos Lançamentos de Entrada e Saída.  
  
Documento auxiliar: [1](https://tdn.totvs.com/pages/viewpage.action?pageId=422545626#BLOCOD-D731)

### Registro D735 - Observações do lançamento fiscal (Código 62)

Estas informações equivalem às observações que são lançadas na coluna “Observações” dos Livros Fiscais previstos no Convênio SN/70 – SINIEF, art. 63, I a IV.

Documento auxiliar:

### Registro D737 - Outras obrigações tributárias, ajustes e informações de valores proveniente de documento fiscal (Código 62)

Este registro tem por objetivo detalhar outras obrigações tributárias, ajustes e informações de valores do documento fiscal do registro D735, que podem ou não alterar o cálculo do valor do imposto.

Documento auxiliar:

## Movimento

**Campo Chave de Acesso**  
  
Nos movimentos de Entrada a chave de Acesso deve ser preenchida na pasta NFcom.

Imagem

O campo **Chave de Acesso** será exibido quando o **Tipo Movimento de Entrada** estiver parametrizado como **Não integrado** para a NFcom utilizando o código modelo de documento 62, conforme imagem:

Imagem

A chave de acesso dos Movimentos de Saída fica na própria nota, ao Escriturar o Movimento de saída será considerada essa chave.

Imagem

## Lançamento

**Campo Chave de Acesso**  
  
A chave de acesso será preenchida no lançamento fiscal ao escriturar o movimento e está disponível em **Informações Adicionais** pasta **Outros**:

Imagem
