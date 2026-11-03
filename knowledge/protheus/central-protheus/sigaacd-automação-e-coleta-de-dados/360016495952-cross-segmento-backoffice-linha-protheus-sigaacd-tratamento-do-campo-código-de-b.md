---
article_id: 360016495952
category: SIGAACD - Automação e Coleta de Dados
content_hash: 1f6b838315cb46447bbdf92a94fb8564ab7927dd4aee727242baa217f2f76c61
fetched_at: '2026-06-28T22:39:11.149791+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD -  Tratamento do Campo
  "Código de Barras" no cadastro de produtos
type: support-article
updated_at: '2021-11-29T14:07:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016495952-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Tratamento-do-Campo-C%C3%B3digo-de-Barras-no-cadastro-de-produtos
---

**Dúvida**Quando realizado o cadastro de produtos com código de Barras (ean-13) completo, o sistema adiciona um dígito a mais. Existe alguma maneira de desabilitar este dígito verificador?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**O campo "Cod.de Barras" (B1\_CODBAR) foi criado para utilização na integração com as rotinas de Automação e Coleta de Dados, para que seja identificado o código de barras a ser adotado pelo sistema quando for necessária a impressão de etiquetas de produtos.  
  
Caso em seu processo não seja necessário o uso deste dígito verificador, realize o seguinte procedimento:

1. Acesse o módulo configurador (SIGACFG) - Base de Dados - Dicionário - Gatilhos;  
2. Pesquise o campo B1\_CODBAR;  
3. Altere o gatilho do campo conforme abaixo:  
  
Campo Regra:  
  
Com digito verificador= trim(m->b1\_codbar)+eandigito(trim(m->b1\_codbar))  
Sem digito verificador= trim(m->b1\_codbar)  
  
![DIGITO.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360012736852/DIGITO.PNG)

Com essa configuração, por padrão assim que efetuar procedimentos no Coletor de Dados ou App "Meu Coletor de Dados", ao escanear o Código de Barras do produto o Sistema fará um vínculo com o campo cadastrado no Produto (B1\_CODBAR) para lançar o produto em questão.

Caso o usuário faça o controle por Etiquetas (tabela CB0), deve-se configurar o parâmetro MV\_ACDCB0, onde é possível definir a maneira que será impressa a etiqueta (ou seja, baseando em uma determinada informação):

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Tipo** | **Descrição** |
| MV\_ACDCB0 | Caracter (C) | Neste parâmetro devem ser informados os tipos de etiquetas que irão utilizar o código interno (CB0) para controle de codificação. Tipos usados: '01' - produto '02' - localização/Endereço '04' - usuário '05' - volume saída '06' - transportadora '07' - volume entrada Ex.: Para se utilizar um controle de codificação para produtos e localização/endereço, o parâmetro deverá ser preenchido da seguinte forma: 01\*02 |

**Saiba Mais**

*[Campo B1\_CODBAR do Cadastro de Produtos](http://tdn.totvs.com/display/public/PROT/Campo+B1_CODBAR+do+Cadastro+de+Produtos)*

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados (ACD)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
