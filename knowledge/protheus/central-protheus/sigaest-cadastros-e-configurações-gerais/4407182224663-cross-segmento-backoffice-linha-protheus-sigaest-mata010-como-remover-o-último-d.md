---
article_id: 4407182224663
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 4c29dd016305fc0f5678e46a3564c5933a16d4bc94687577553e390091b3642a
fetched_at: '2026-06-28T22:39:09.471929+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como remover
  o último dígito automático do Código de Barras?
type: support-article
updated_at: '2023-10-13T23:06:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407182224663-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-remover-o-%C3%BAltimo-d%C3%ADgito-autom%C3%A1tico-do-C%C3%B3digo-de-Barras
---

**Dúvida**Ao realizar o Cadastro de um Produto com código de Barras completo, o sistema adiciona um dígito a mais. Existe alguma maneira de desabilitar este dígito verificador?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O campo "Cod.de Barras" (B1\_CODBAR) foi criado para utilização na integração com as rotinas de Automação e Coleta de Dados, para que seja identificado o código de barras a ser adotado pelo sistema quando for necessária a impressão de etiquetas de produtos.  
  
Caso em seu processo não seja necessário o uso deste dígito verificador, realize o seguinte procedimento:

1. Acesse o módulo configurador (SIGACFG) - Base de Dados - Dicionário - Gatilhos;  
2. Pesquise o campo B1\_CODBAR;  
3. Altere o gatilho do campo conforme abaixo:  
  
Campo Regra:  
  
Com digito verificador= trim(m->b1\_codbar)+eandigito(trim(m->b1\_codbar))  
Sem digito verificador= trim(m->b1\_codbar)

![DIGITO.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360012736852/DIGITO.PNG)

**2° alternativa - Via Parâmetro**

Outra alternativa para que não seja calculado o digito verificador no campo Código de Barras (B1\_CODBAR) seria por meio do parâmetro **MV\_EANCALC**, que indica se o dígito verificador (último dígito) será calculado ao preencher os demais dígitos no campo. Se configurado como **.T.**, o parâmetro fará com que o dígito verificador seja calculado e adicionado ao final do número informado no campo. Caso configurado como **.F.**, o dígito verificador não será calculado, mantendo assim apenas os números já inseridos no campo.

**Procedimento para criação do parâmetro**

No Configurador (SIGACFG), acesse Ambientes / Cadastros / Parâmetros (CFGX017). Crie o parâmetro a seguir:

|  |  |
| --- | --- |
| **Itens** | **Conteúdo** |
| **Nome** | MV\_EANCALC |
| **Tipo** | L |
| **Cont. Português** | .T. |
| **Descrição** | Define se o dígito verifcador do código de barras será calculado. .T. = Sim; .F. = Não |

**Saiba Mais**

*[Campo B1\_CODBAR do Cadastro de Produtos](http://tdn.totvs.com/display/public/PROT/Campo+B1_CODBAR+do+Cadastro+de+Produtos)*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
