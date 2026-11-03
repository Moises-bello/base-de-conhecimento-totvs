---
article_id: 360058068794
category: TAF - eSocial - Atualização
content_hash: 506635aba25ea616f913c063d352763399dc024add3d0305d82713af3a4dbd50
fetched_at: '2026-06-28T22:45:13.395121+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Atualização - Como utilizar Migrador
  no TAF
type: support-article
updated_at: '2026-06-26T11:13:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058068794-RH-Linha-Protheus-TAF-eSocial-Atualiza%C3%A7%C3%A3o-Como-utilizar-Migrador-no-TAF
---

**Dúvida**

Como realizar a migração dos eventos transmitidos anteriormente de um software terceiro para o TAF e-Social?

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Atualização - Migrador -  À partir da release 12.1.33 e superiores

**Solução**

**Premissas para migração**

1 - Para realizar a migração de softwares terceiros para o TAF, é obrigatório a criação da empresa no sistema, conforme documentação abaixo:

[TAF - CONFIGURAÇÃO - Criação de Empresas e Filiais (Gestão de Empresas)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034612553)

2 - Após criar a empresa, efetue a amarração de empresas quando *logar* no TAF:  
[MP - TAF - Amarração Complemento de Empresa - TAFA050 - TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034976434-MP-TAF-Amarra%C3%A7%C3%A3o-Complemento-de-Empresa-TAFA050-TAF)

3 - Em seguida deve-se criar o complemento de empresas:  
[TAF - COMPLEMENTO DE EMPRESAS - Como acessar o complemento cadastral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034612553)

4 - Realize o ajuste de recibo no TAF para o evento S-1000:  
[TAF - FUNCIONALIDADES - Como realizar ajuste de recibo do e-Social no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-TAF-FUNCIONALIDADES-Como-realizar-ajuste-de-recibo-do-e-Social-no-TAF)

**Obs.**: É necessário fazer o ajuste de recibo para o evento S-1000 pois o migrador NÃO executa a esta rotina para este evento.

5 - É necessário todos os **XML's** de Envio e Retorno gerados em arquivos pelo software responsável pelo envios ao E-Social;

6 - O XML de Envio ao RET deverá ser iniciado pelo node principal **<eSocial>**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100721053)

7 - O XML de retorno do e-Social deve ter obrigatoriamente o node **<retornoEvento>**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098514454)

**Importante:**Codificação do arquivo:

Todos os **XML's**, obrigatoriamente devem ficar no formato **UTF-8** igualmente especificado no manual do desenvolvedor e-social na seção Padrão Técnicos.

8 - Após obter todos os XML's, será necessário criar a seguinte estrutura de pasta no diretório informado na seção **RootPath** da instalação nova do TAF.   
Conforme exemplo abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098514694)

Exemplo da estrutura de pasta:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100760713)

9 - Após a construção da estrutura de diretórios acima, iremos acessar a seguinte opção no menu do SIGATAF. Clique em Miscelânea -> Funcionalidades -> Migrador:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098578994)

10 - Será exibido a tela abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098579074)

**Obs.:** Nesta tela temos as seguintes opções:  
  
**Processar**: Esta é a rotina responsável por migrar os arquivos presentes nas pastas para o TAF.  
**Relatório**: Esta opção é responsável por extrair um relatório com as informações migradas após realizarmos o processo de migração.  
**Visualizar**: Esta opção visualiza registros específicos presentes no browse após o processo de migração.

11 - Ao utilizarmos o botão Processar será apresentado o *Wizard* abaixo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098579194)

12 - Ao clicar em Avançar será apresentado no **wizard** a seguinte tela:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100816293)

**Obs.: Tipos de Execução:**

**Somente Importar:** Esta opção irá realizar o envio dos XMLs presentes nas pastas para a tabela temporária do TAF, ao utilizar esta opção apenas a tabela temporária do TAF será gerada, não realizando assim nenhuma integração com as tabelas dos Eventos do E-Social no TAF.

**Somente Processar**: Esta opção irá realizar o envio dos registros presentes na tabela temporária gerada utilizando a opção Somente Importar para as tabelas dos respectivos eventos do E-Social. Esta opção deve ser utilizada somente após a opção Somente Importar ter sido executada.

**Importar e Processar:** Esta opção irá realizar ambos os processos em uma única execução.

**Nº de Threads:** Este parâmetro é utilizado para informar quantas threads serão utilizadas durante o processo de migração, este número pode variar entre 1 e 10.

**Diretório:** Nesta opção iremos informar o diretório configurado nas premissas de migração.

13 - Na imagem abaixo clicamos em Importar e Processar e em seguida Processar:

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098580354)**

14 - Ao fim do processo, clique em Concluir e no ***browse*** será exibido as informações de todos os eventos integrados ao TAF:

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098580374)**

15 - Verifique se os eventos estão em suas devidas rotinas com o número de recibo preenchido.
