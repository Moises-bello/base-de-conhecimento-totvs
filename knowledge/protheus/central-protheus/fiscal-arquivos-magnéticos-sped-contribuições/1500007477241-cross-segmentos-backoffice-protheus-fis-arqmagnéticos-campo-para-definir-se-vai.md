---
article_id: 1500007477241
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 1ded7fc9da0301d8ace96beb1bd2fe8bc3c8286c636a9b62835d8268e46b193b
fetched_at: '2026-06-28T22:42:04.936794+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Campo para definir
  se vai gerar os blocos F100 e 0111 ou somente F100 no Efd Contribuições
type: support-article
updated_at: '2022-08-31T12:56:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007477241-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Campo-para-definir-se-vai-gerar-os-blocos-F100-e-0111-ou-somente-F100-no-Efd-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como configurar o Protheus para gerar os blocos **F100** e **0111** ou somente o bloco **F100** no **Efd** **Contribuições**?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Incluso campo **ED\_F100** no cadastro de **natureza** tabela SED para que seja possível o cliente escolher se irá gerar o bloco **F100** e  **0111** ou somente o bloco **F100;**

**Atenção:**

Esta alteração não descarta os cadastros para geração do bloco **F100;**

1. Criação de Campos no arquivo SX3 – Campos, filtrando a Tabela SED - Cadastro de **Natureza**;

|  |  |
| --- | --- |
| **Campo** | ``` ED_F100 ``` |
| **Tipo** | ``` Caractere ``` |
| **Tamanho** | ``` 1 ``` |
| **Decimal** | ``` 0 ``` |
| **Formato** | ``` @! ``` |
| **Título** | ``` Gera F100 ``` |
| **Descrição** | ``` Gera arquivo F100 ``` |
| **Usado** | ``` Sim ``` |
| **Obrigatório** | ``` Não ``` |
| **Browse** | ``` Sim ``` |
| **Opções** | ``` 1=Sim ; 2= Não ``` |
| **Help** | ``` Indica se será gerado o Bloco F100 e o bloco 0111 (Sim), ou somente o bloco F100 (não) ``` |

2. Procedimento para Utilização;

- No módulo financeiro, alterar uma **natureza** configurada para gerar o bloco **F100** e alterar o campo **ED\_F100** = Não;

- Incluir um título a receber no financeiro;

3. Gerar apuração **Efd Contribuições**;

4. Gerar o arquivo **Efd Contribuições**;

5. Verifique que o título não foi somado no bloco **0111** ou seja só vai gerar o bloco **F100**;

Mais informações no link abaixo:

https://tdn.totvs.com/display/public/PROT/TUNABV\_DT\_Bloco\_F100\_e\_bloco\_0111
