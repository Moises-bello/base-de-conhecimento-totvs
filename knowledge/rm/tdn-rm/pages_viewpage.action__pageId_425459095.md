---
content_hash: 56e99eb3462a67b56043268f14296d9589eb5d744d3cd984680dedb61d4d178d
fetched_at: '2026-06-29T00:09:33.963465+00:00'
page_id: '425459095'
product: rm
source: tdn-rm
title: Parâmetros de Marketing
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459095
version: 1
---

**Parâmetros de Marketing**

---

Os parâmetros da campanha são campos extras que podem ser customizados de acordo com as regras de negócio da empresa. Eles funcionaram de forma similiar ao cadastro de parâmetros do tipo de atendimento. De diferentes tipos de formato, eles atendem a necessidade gravar informações suplementares às pré-definidas no atendimento. Os formatos podem ser:  
   
**Inteiro** = Valores numéricos inteiros.  
Ex: Quantidade dias para vigência da campanha = 10.  
   
**String** = Informações textuais, sendo necessário limitar o tamanho do parâmetro em caracteres.  
Ex.: Complemento da Campanha = Esta solicitação possui autorização do gestor da área e será estendida as unidades filiais.  
   
**Real** = Valores numéricos fracionados. Números Decimais.  
Ex.: Valor da Confecção dos Planfletos = R$ 1000,00.  
   
**Data** = Informação referente ao tempo. Dia/Mês/Ano.  
Ex.: Data Nascimento Cliente = 01/01/1980.  
   
**Texto** = Informações textuais sem limitação pré-definida.  
Ex.: Informações Adicionais da Campanha = Todas as documentações necessárias foram enviadas em formato digital. Favor confirmar resolução das propagandas e quantidade de arquivos enviados.  
   
**Lógico** = Informações para serem marcadas através de flag´s (Checkbox).  
Ex.: Possui filhos?   X Sim      Não  
   
**Link** = Informações que ligam a outros componentes. Ele se subdivide em:

* *E-mail* = Endereço eletrônico para troca de mensagem. Aciona automaticamente o gerenciador de email padrão da máquina. Ex.: [teste@teste.com.br](mailto:teste@teste.com.br)
* *URL* = Aciona o navegador padrão do sistema com o endereço digitado. Ex.: [{+}](http://www.totvs.com/)<http://www.totvs.com+>
* *SkypeLink* = Endereço do usuário de Skype, utilizado para comunicação de voz, vídeo, troca de mensagens entre outros. Aciona o Skype com o endereço informado. Ex.: Usuário = teste.skype

**Observação**   
Para os tipos de parâmetros igual a link é necessário limitar o tamanho do parâmetro em caracteres.   
Para realizar o cadastro desses parâmetros:  Marketing->Parâmetros de marketing   
Para associá-los a uma campanha : Marketing->Campanha  | Anexo Parâmetros da campanha.   
Visualizar e Manipular os parâmetros: Meus atendimentos->Operações de telemarketing | "Executar operação de telemarketing".
