---
content_hash: d6e4ad4f861eed1364be0a9c0f53d19ce2641a248813c443a2218dd5ae0dcc01
fetched_at: '2026-06-29T00:05:57.049799+00:00'
page_id: '161351622'
product: rm
source: tdn-rm
title: RMCTB00006_Exportação e Importação do Plano de Contas Referencial entre Coligadas
  Layout 2.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=161351622
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Gestão Patrimonial – **Versão:** 11.52 |
| **Processo** | : | Exportação e Importação do Plano de Contas Referencial entre Coligadas |
| **Subprocesso** | : | SPED Contábil |
| **Data da publicação** | : | 12/09/2014 |

**Introdução**

É possível exportar o Plano de Contas Paralelo já associado com o plano de contas contábil de uma coligada origem para uma coligada destino.  
 Esse processo tem como objetivo facilitar a vinculação dos Planos de Contas Referenciais entre coligadas que possuem a mesma parametrização do Plano de Contas Contábil.

**Desenvolvimento/Procedimento**

**Exportação**  
 Realize a Importação do 'Plano de Contas Referencial' na Coligada origem, através do seguinte procedimento:

a) Acesse 'Relatórios' / 'Gerador';

b) Edite o relatório '04.006 Exportação Plano de Contas Paralelo', conforme imagem abaixo:

c) Clique duas vezes sobre o campo "DESCRIÇÃO DA CONTA DO PLANO PARALELO" para visualizar as 'Propriedades' correspondentes;

d) Na guia 'Preenchimento' altere o 'Número de Caracteres' para '100' e salve alterações realizadas, conforme imagem abaixo:

e) Gere o relatório em questão em arquivo texto.

**Importação:**  
 Realize a Importação do 'Plano de Contas Referencial' na Coligada destino, através do seguinte procedimento:

a) Acesse 'Utilitários' / 'Conversões' / 'Importação por texto';

b) Clique no botão 'Padrão' e limpe todos os caminhos indicados na aba Arquivos;

c) Na opção do 'Plano de Contas Paralelo' indique o caminho que o arquivo exportado anteriormente.

d) Na guia 'Plano de Contas Paralelo' informe um código, uma descrição e a máscara do plano referencial.

e) 'Importar'

Conforme exemplo abaixo:

**Informações adicionais:**

Vale ressaltar que os 'Processos' citados são definidos no perfil do usuário. Obs.: 'Cadastros' / 'Segurança' / 'Perfis' / 'Acesso a Menus' / 'RM Saldus'.   
 Durante o processo de importação do 'Plano de Contas Referencial' informe um 'Código' único e sem zeros à esquerda para impedir duplicações.   
 Vale ressaltar que caso uma ou mais Contas Contábeis não sejam efetivamente vinculadas, será necessário realizar o vínculo do 'Plano de Contas Contábil' com o 'Plano de Contas da Referencial' manualmente.

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE** [**R@Controladoria**](http://fluig.totvs.com/portal/p/10097/subject/rcontbil)

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 5 – (Planejamento e Controle Orçamentário), 2 – (RM Saldus).
