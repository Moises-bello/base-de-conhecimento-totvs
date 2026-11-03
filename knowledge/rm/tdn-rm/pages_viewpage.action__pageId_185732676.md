---
content_hash: 0ce5b2539a176beb205e632677c5a9424fe7a0218c334f64d70f51d1945982ae
fetched_at: '2026-06-29T00:05:58.135139+00:00'
page_id: '185732676'
product: rm
source: tdn-rm
title: Configurar margens no gerador .net.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185732676
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Reports                         **Versão:**11.8x |
| **Processo** | **:** | Configurar margens no gerador .net. |
| **Subprocesso** | **:** | Informações da Página |
| **Data da publicação** | **:** | 23/02;2015 |

 Consideramos que as medidas do gerador Report está em Decímetros.

Exemplo: Para uma altura de 2 centímetro, considera 200 / 100.

**Configurando o tamanho de página do relatório**

O Gerador Report, utiliza o drive da impressora, considerando o papel definido pela mesmo ou personalizado no servidor de aplicação da impressora.

No gerador faça:

1. Propriedades do relatório:

No exemplo acima, em Definições da Página, selecionamos **Tipo do Papel** A4. Observe que automaticamente a **Altura da Página** está 2969 ou 29cm.

1. Alterando as margens da impressora.

Nas propriedades do relatório > Definições de Página > Margens.   
   
  
   
 Direta: Margem direita do relatório;  
 Esquerda: Margem esquerda do relatório;  
 Fundo: Final do relatório;  
 Topo: Inicio do Relatório.   
 Exemplo: O valor 254 da margem esquerda do relatório, significa 2,5 cm aproximada mente de margem\_GoBack a direita.

1. Definindo o tamanho dos grupos.

Nas propriedades do detalhe, altere a altura na opção de Layout.   
   
  
   
No exemplo acima, definimos a altura como 200, ou seja, 2 centímetros.

Função de Posição Inicial ou Posição final.

Considerando o print acima, se marcamos para Posição inicial 150, os dados do detalhe iniciarão na posição 1,5 centímetros.
