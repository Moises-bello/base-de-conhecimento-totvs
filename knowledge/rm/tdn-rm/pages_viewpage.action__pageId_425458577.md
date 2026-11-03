---
content_hash: 1638a664dc447c210175bee8ccc83e0cfd8286c45eb3e92d28e6fe895e5f9d4e
fetched_at: '2026-06-29T00:09:31.247775+00:00'
page_id: '425458577'
product: rm
source: tdn-rm
title: Parâmetros da Pesquisa de Satisfação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458577
version: 5
---

**Parâmetros da Pesquisa de Satisfação**

---

Os parâmetros da pesquisa de satisfação são os campos que serão apresentados na pesquisa. Quando o atendimento atinge o status de concluído respondido um e-mail é disparado com o link para acesso à pesquisa. Eles podem ser customizados de acordo com as regras de negócio da empresa. Possuem funcionamento parecido aos parâmetros do tipo de atendimento. De diferentes tipos de formato, eles atendem a necessidade gravar informações de diversos tipos. Os formatos podem ser:

**Inteiro** = Valores numéricos inteiros.  
 Ex: Quantidade Dias para Solução Atendimento = 10.  
    
 **String** = Informações textuais, sendo necessário limitar o tamanho do parâmetro em caracteres.  
 Ex.: A quantidade de dias para solução do atendimento foi satisfatória? Por que ? = A quantidade de dias gastas para solução do problema foi satisfatória porque foi verificada antes do prazo previsto.  
    
 **Real** = Valores numéricos fracionados. Números Decimais.  
 Ex.: Nota para o atendimento (1 a 10)= 9,5.  
    
 **Data** = Informação referente ao tempo. Dia/Mês/Ano.  
 Ex.: Data Término do Atendimento = 14/08/2011.  
    
 **Texto** = Informações textuais sem limitação pré-definida.  
 Ex.: Informações Complementares = Todas as documentações necessárias foram enviadas em formato digital. Por esse motivo, a avaliação dos documentos ocorreu de forma rápida.  
    
 **Lógico** = Informações para serem marcadas através de flag´s (Checkbox).  
 Ex.: Você está satisfeito com a solução proposta?   X Sim      Não  
    
 **Link** = Informações que ligam a outros componentes. Ele se subdivide em:

* *E-mail* = Endereço eletrônico para troca de mensagem. Aciona automaticamente o gerenciador de email padrão da máquina. Ex.: [teste@teste.com.br](mailto:teste@teste.com.br)
* *URL* = Aciona o navegador padrão do sistema com o endereço digitado. Ex.: [{+}](http://www.totvs.com/)<http://www.totvs.com+>
* *SkypeLink* = Endereço do usuário de Skype, utilizado para comunicação de voz, vídeo, troca de mensagens entre outros. Aciona o Skype com o endereço informado. Ex.: Usuário = teste.skype

**Observação:**

Para os tipos de parâmetros igual a link é necessário limitar o tamanho do parâmetro em caracteres.   
 Setenças SQL e actions também podem ser vinculadas.

Ex: SELECT ASSUNTOOC, CODATENDIMENTO , CODCOLIGADA, CODLOCAL , CODATENDIMENTO FROM HATENDIMENTOBASE Nesse exemplo,  o parâmetro é montado na forma padrão como  lookup . Ele irá utilizar a primeira coluna ASSUNTOOC para ser a descrição do lookup , a segunda coluna CODATENDIMENTO como o código do lookup.  
 E ao associar a Action de atendimento CRMATENDIMENTOEXTACTION a essa sentença a chave primária da action será associada as colunas da sentença no caso a chave primária do atendimento (CODCOLIGADA , CODLOCAL , CODATENDIMENTO).
