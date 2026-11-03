---
content_hash: 712405a0cba0bdc277200697b7842df695333d8af09250b83685fe28f13c9307
fetched_at: '2026-06-29T00:05:55.036560+00:00'
page_id: '120784504'
product: rm
source: tdn-rm
title: Criação da Tabela de Cálculo IRRF PLR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=120784504
version: 5
---

**Atenção! Procedimento válido para versões 11.52 e superiores**

Para criação da tabela de cálculo de IRRF para PLR, primeiro precisa ser cadastrada uma nova tabela acessando o menu *Cadastros I Cálculos I Tabelas de cálculo*

Cadastrar a seguinte tabela de cálculo:  
 **Código:** IRPLR  
 **Finalidade:** 4 – IRRFPL  
 **Início da vigência:** 01/01/2013   
 **Fim da vigência:** 31/12/2013  
 **Descrição:** TABELA IRRFPLR 01/2013 – 12/2013

*Obs.: Criar uma nova tabela para o ano 2014 alterando as datas de vigência em caso de alteração nos valores da tabela.*

Na aba "Valores da Tabela" deverá inserir os valores da tabela de IRRF sobre Participação nos Lucros.  
Esta tabela está disponível em: <http://www.receita.fazenda.gov.br/Legislacao/MPs/2012/mp597.htm#Anexo>

Abaixo está um exemplo da tabela cadastrada:   
   
  
   
   
 Em seguida, acessar o menu *Cadastros I Cálculos I Valores Fixos*.   
 Confirmar se existe o valor fixo DDEP – Valor a deduzir de IRRF por dependente, com vigência no ano corrente.

Após a criação das tabelas, verificar se existem cadastrados os seguintes eventos:  
• *PARTICIPAÇÃO NOS LUCROS – **CC 126***  
*• IRRF PARTICIPAÇÃO NOS LUCROS – **CC127***  
*• DEDUTÍVEL IRRF PARTICIPAÇÃO NOS LUCROS – **CC 143***  
*• PENSÃO ALIMENTÍCIA PARTICIPAÇÃO NOS LUCROS – **CC 121***

Caso os eventos não estejam cadastrados, gentileza cadastrar conforme prints abaixo:  
 Obs: Lembrando que o código do evento pode ser definido conforme desejo da empresa.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[R@RH](https://totvs.byyou.com/?space=rrh)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 4 – (Recursos Humanos)
