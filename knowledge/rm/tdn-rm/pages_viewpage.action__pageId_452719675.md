---
content_hash: 9d6e81796cb48ccc989dbe68885f08b88117a8b53b71a67be6dc1e35cff6571f
fetched_at: '2026-06-29T00:10:09.459717+00:00'
page_id: '452719675'
product: rm
source: tdn-rm
title: Funções a Desconsiderar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719675
version: 3
---

Através desde cadastro o usuário poderá incluir as funções que serão desconsideradas no evento S-1030 - Tabela de Cargos.   
    
 **Atenção:**  
 Sempre que o usuário realizar uma alteração de função ou incluir um novo funcionário utilizando uma função que esteja parametrizada para não ser considerada será gerado os eventos S-2206 -Alteração de Contrato de Trabalho ou S-2200- Admissão /Ingresso de Trabalhador .  
    
 **Exemplo:**  
 Alterada função:  
 De:     Função 1234-Analista  
 Para:  Função 0001- Técnico (Função cadastrada no Parametrizador)  
 Após concluir o processo será gerado o evento S-2206 -Alteração de Contrato de Trabalho  com o código de cargo = "0001" .

|  |
| --- |
| Informações Complementares |

---

eSocial

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)
