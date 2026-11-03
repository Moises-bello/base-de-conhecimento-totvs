---
article_id: 360034765854
category: TAF - eSocial - Atualização
content_hash: 9ae9d539302de9dc270ea2066016e345a03650cd560c277f2c93b100707fe9e0
fetched_at: '2026-06-28T22:45:13.326550+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - ATUALIZAÇÃO - Executando UPDDISTR
type: support-article
updated_at: '2026-06-23T11:43:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034765854-RH-Linha-Protheus-TAF-eSocial-ATUALIZA%C3%87%C3%83O-Executando-UPDDISTR
---

**Dúvida**  
Como executar o compatibilizador UPDDISTR?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - À partir da release 12.1.33  
  
**Solução**

***Nota Importante:***

Antes de iniciar o processo com o UPDDISTR, é crucial que o serviço TAF-WS esteja desligado e nenhum usuário esteja conectado ao sistema.

1. **Preparação Inicial:**
   * Certifique-se de que o arquivo APPSERVER.INI, localizado na pasta bin/appserver, contenha a seção [ONSTART]. Se a seção existir, coloque um ponto e vírgula antes (;[ONSTART]) para comentá-la. Salve essa alteração. Depois disso, reinicie o appserver do TAF para aplicar a alteração.
2. **Iniciar o Processo:**
   * Abra o SmartClient do TAF e no campo "Programa Inicial", digite "UPDDISTR":
   * ![](https://centraldeatendimento.totvs.com/hc/article_attachments/41423233541783)
3. **Atualização de pacotes e metadados:**
   * Será informado sobre a execução da atualização com o objetivo de compatibilizar o dicionário de dados e as tabelas. Clique em avançar:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22967964780567)
4. **Termo de aceite:**
   * Será exibido um termo de aceite para compatibilização do dicionário. Clique em avançar:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22967970986007)
   * Na próxima tela ainda sobre o termo de aceite recomenda-se a leitura do termo. Após a leitura, basta marcar a opção "Li e aceito todas as novidades e mudanças da nova versão / release" e clique em avançar:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969260499223)
   * Realize o backup da pasta do Protheus ou TAF e do seu banco de dados. Assim que for feito o backup, basta marcar as opções de Backup para avançar:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969248485783)
   * Para quem for Protheus e tiver customização, realize o backup dos arquivos RPO's, caso for TAF Segregado, pode marcar a opção que não possui customizações:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969260529431)
   * Selecione o país que está realizando a atualização do sistema e clique em avançar:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969248509719)
   * Avance a tela:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969260555287)
5. **Login e senha:**
   * O sistema pedirá usuário e senha do administrador do sistema. e clique em avançar:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969260565527)
6. **Informação sobre o arquivo de atualização:**
   * Nesta será exibido o que será atualizado, se será a expedição contínua ou se será realizado a migração de release do sistema:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969248564375)
7. **Diretório de dados:**
   * Informe o diretório de dados para criação de novas tabelas de cada grupo de empresas relacionado:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969260586775)
8. **Configuração:**
   * Marque as opções da configuração do LOG para sejam informados tudo o que ocorre durante a atualização conforme exemplo na figura abaixo:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969260594199)
   * Clique em avançar;
   * Nesta tela serão informados quais atualizações serão realizadas:  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969248595479)
9. **Execução:**
   * Será executado o processo de compatibilização e criação de novas tabelas  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969248607895)
10. **Finalização:**
    * Estando tudo ok, será apresentado que foi atualizado com sucesso e clique em finalizar:  
      ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22969260621079)
    * Reincie o TAF-WS e descomente a seção [ONSTART] do APPSERVER e reinicie o APPSERVER.

Ao seguir essas etapas de forma cuidadosa, você poderá atualizar o sistema de maneira eficaz utilizando os programas UPDDISTR. Certifique-se de seguir as orientações de pré-requisitos e etapas com atenção para garantir um processo de atualização bem-sucedido.
