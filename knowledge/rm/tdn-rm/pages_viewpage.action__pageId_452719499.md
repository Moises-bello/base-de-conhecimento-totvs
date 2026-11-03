---
content_hash: e9a25afe545ade10b3f30f90039a2fb306b4d2289f6a96c2d9c4d63d1ff5998c
fetched_at: '2026-06-29T00:10:08.032215+00:00'
page_id: '452719499'
product: rm
source: tdn-rm
title: Seções a Desconsiderar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719499
version: 2
---

Através deste cadastro o usuário poderá incluir as seções que serão desconsiderados nos eventos S-1005 - Tabela de Estabelecimentos e Obras e S-1020 - Tabela de Lotações Tributárias.  
    
 **Observações:**  
 Carga inicial: Na carga inicial ao gerar os eventos 1005 e 1020 (no caso do 1020 quando não utilizar tomador) o produto não irá considerar as seções que estiverem inativas, sendo assim, não irá gerar os gatilhos iniciais para estas seções.  
    
 Validação da base de dados:  Na validação da base de dados ao gerar os eventos 1005 e 1020 (no caso do 1020 quando não utilizar tomador) o produto não irá considerar as seções que estiverem inativas, sendo assim, caso seção possua algum erro cadastral, o erro não será apresentado no validador devido a seção não ser considerada.  
    
 Geração do XML dos eventos que usam Seção/Lotação: Na geração dos eventos S-1200, S-2299 e S-2399, quando não utiliza tomador de serviço o sistema irá verificar se a seção do funcionário é inativa ou a desconsiderar, caso sim irá ser adicionado uma mensagem de erro no log "Erros de geração" informando que a seção do funcionário não está inativa. Para o evento S-2200, quando o funcionário possuir código de categoria diferente de 104 e 106, será feita a validação em cima da filial da seção no qual o funcionário se encontra alocado, caso esteja desativada será adicionado uma mensagem de erro no log.  
    
 **Atenção:**  
 No processo de "Gerar lotações tributarias" será ignorada as seções inativas ou a desconsiderar, porém caso o funcionário possua movimentação por tomador ou histórico de afastamento com tomador vinculado, e sua filial se encontrar inativa/Desconsiderada, o sistema irá gerar a lotação tributaria não ignorando a filial inativa.  
    
 Para as filias que foram inativadas/desconsideradas e consequentemente ignoradas pela Carga Inicial, caso a mesma volte a ficar ativa ou desvinculada das seções a desconsiderar, sua inclusão na fila de eventos deverá ser feita manualmente.  
    
 Ao executar algum processo que gere lotação tributaria, como por exemplo inclusão de rateio por tomador, o sistema não irá tratar as seções inativas, sendo assim será criado uma nova lotação tributaria.

|  |
| --- |
| Informações Complementares |

---

eSocial

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)
