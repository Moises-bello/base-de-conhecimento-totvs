---
content_hash: ac861007714ea94bdc8d4fbf5dc70fae4c1ebd59b151401761ad3ec0370aa9a9
fetched_at: '2026-06-29T00:11:11.437310+00:00'
page_id: '64652568'
product: rm
source: tdn-rm
title: Metadados em 3 camadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Metadados+em+3+camadas
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Inteligência de Negócios                      **Versão:**11.50 |
| **Processo** | **:** | Metadados |
| **Subprocesso** | **:** | Executando Metadados em 3 camadas |
| **Data da publicação** | **:** | 04/07/2013 |

## Executando Metadados em 3 camadas

Este manual tem como objetivo ilustrar o processo de como executar um Metadados em um ambiente 3 camadas.  
 Primeiramente é necessário acessar a Nova MDI na maquina Client. Em seguida acesse o menu Serviços Globais > Metadados > Projetos

Selecione o Projeto e acesse Processos > Gerar Projetos de Metadados 

 Após gerar o Projeto com sucesso, é possível verificar que foram criados os arquivos:   
 • RM.MD.PRJ3004416.Client.dll no diretório C:\totvs\CorporeRM\RM.Net da maquina CLIENT  
 • RM.MD.PRJ3004416.Server.dll no diretório C:\totvs\CorporeRM\RM.Net do SERVER   
 Obs.: Entretanto para que o Metadados seja executado corretamente em 3 camadas é necessário que em ambas as maquinas SERVER e CLIENT estejam presentes as duas DLL's. Sendo assim é preciso copiar a DLL CLIENT para o SERVER e a DLL SERVER para a(s) maquinas CLIENT.   
 Depois dos procedimentos executados acima, basta acessar o diretório C:\totvs\CorporeRM\RM.Net do  
 SERVER, parar o serviço do HOST remover o arquivo \_Broker.dat e reiniciar o serviço do HOST novamente.   
 Ao fim de todo o procedimento será possível executar os Metadados a partir do SERVER e da maquina  
 CLIENT como segue:   
  

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
