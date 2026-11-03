---
article_id: 360044572434
category: RH - Definições de Cálculo
content_hash: ca722416a088f2b8ab2aeba38baeed6ef2a719c46317c39c44e75588f8260fea
fetched_at: '2026-06-28T22:43:22.425628+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como recriar apenas roteiros e fórmulas do módulo
  07 - Gestão de Pessoal - SIGAGPE
type: support-article
updated_at: '2025-03-25T12:48:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044572434-RH-Linha-Protheus-GPE-Como-recriar-apenas-roteiros-e-f%C3%B3rmulas-do-m%C3%B3dulo-07-Gest%C3%A3o-de-Pessoal-SIGAGPE
---

**Dúvida**Como recriar as fórmulas, mnemônicos e roteiros do módulo 07 Gestão de Pessoal (SIGAGPE)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução  
1.** Renomeie a pasta que contém o **repositório de fórmulas (rpofrm),** que fica no diretório do RPO do Protheus (ele é gerado a partir das fórmulas e roteiros do SIGAGPE), em **ambiente de testes**;  
  
**2.** Renomeie as tabelas de fórmulas e roteiros, para que o sistema recrie no padrão:  
-SRY - Roteiros de Cálculo  
-SRM - Itens Roteiro de Cálculo   
-RC2 - Cabeçalho de Fórmulas  
-RC3 - Fórmulas

Acesse o **Configurador (SIGACFG)**, entre em **Base de Dados> Dicionários> Base de Dados**. Selecione no canto superior esquerdo Dicionário de Dados e depois selecione o ícone com o símbolo de lupa:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16650219123351)  
  
Será apresentada a tela abaixo. No campo de pesquisa, digite SRY e clique em Buscar. Depois selecione o ícone **Editar:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16650231874967)  
  
No exemplo abaixo, a tabela **SRY** possui o nome **SRYT10**, altere para um nome que não exista em seu ambiente, **SRYT10\_T** por exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16650219137687)  
  
Após a alteração, o campo Nome será alterado como **SRYT10\_T**. Clique em Confirmar. **Faça isso para todas as tabelas listadas acima**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16650219143703)

Será apresentado o *browse*novamente. Clique no ícone com desenho Disquete. Será aberta uma nova janela, clique em Avançar em todas as janelas que forem mostradas:  
**IMPORTANTE: Esta ação depende de acesso exclusivo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16650219147799)**  
Será apresentada a janela abaixo ao fim do processamento. Verifique se será apresentada a mensagem:**Atualização finalizada com sucesso** e Finalize **![](https://centraldeatendimento.totvs.com/hc/article_attachments/16650231904791)**

Após a execução do processo acima com todas as tabelas citadas, acesse o sistema no módulo SIGAGPE para que as mesmas sejam recriadas, nesta ordem:

* Atualizações - Def. de Cálculo - Fórmulas
* Atualizações - Def. de Cálculo - Roteiros de Cálculo

**Este processo demorará alguns minutos.  
  
3.** Após isso, valide se o cálculo/processo ficou correto, **caso problema persista**, deverá realizar o mesmo procedimento acima novamente, mas acrescentando a tabela RCA-Mnemônicos (faça um backup da tabela antes).  
Após renomear a tabela RCA, entre na rotina Atualizações > Def. de Cálculo > Mnemônicos para dar carga.  
  
Após isso, verifique se o cálculo/processo ficou correto, caso fique, retorne no ticket informando que o processo deu certo apenas após o passo 3.

**IMPORTANTE:** Após procedimentos acima, é necessário subir novamente as customizações em roteiros, mnemônicos e fórmulas, pois o processo acima recria os roteiro e fórmulas no padrão, logo as customizações serão perdidas e será necessário retorná-las.  
  
**Saiba Mais**  
[Artigos Gestão de Pessoal](%C2%A0%C2%A0https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
