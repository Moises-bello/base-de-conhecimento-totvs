---
content_hash: f07930f4b8b323026ff257c1599de456a2ba4a6d3af64370a3f102b266758596
fetched_at: '2026-06-29T00:10:10.434225+00:00'
page_id: '452719836'
product: rm
source: tdn-rm
title: S-1020 - Tabela de Lotações Tributárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719836
version: 6
---

Através deste evento geramos informações de lotações tributárias que identificam a classificação da atividade para fins de atribuição do código FPAS, a obra da construção civil, o contratante do serviço, ou uma condição diferenciada de tributação. Lotação tem o conceito estritamente tributário e não físico.  
    
 O arquivo contém informações do Cadastro de Seções e do Cadastro de Lotações Tributárias para quem trabalha com Tomador de Serviço. Para mais detalhes,veja também o help do cadastro de [Seções](http://tdn.totvs.com/pages/viewpage.action?pageId=452719324) e [Lotação Tributária](http://tdn.totvs.com/pages/viewpage.action?pageId=452719593)  
 Serão consideradas as centralizadoras e as seções que atendam a quebra de FPAS onde o campo FPAS esteja preenchido.  
 **Exemplo:**  
 Quebra de FPAS: ?????  
 Seções:01                      
             01.01                   
             01.01.01  
  O sistema irá considerar o FPAS da seção 01.01 conforme quebra.  
  Veja no Parametrizador em Configurações Gerais do eSocial as regras do Código de quebra de FPAS.  
    
    
 [**Mapeamento das informações do evento**](http://tdn.totvs.com/display/LRM/Evento+S-1020)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Eventos Iniciais

Eventos de Tabelas

Gerar XML
