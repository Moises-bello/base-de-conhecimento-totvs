---
content_hash: c2c22cc9d2222136533c6c96b4e9013f8f46f8e448e480341f053d2267bc1e9f
fetched_at: '2026-06-29T00:10:07.337705+00:00'
page_id: '452719405'
product: rm
source: tdn-rm
title: Gerar Carga Inicial
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Carga+Inicial
version: 4
---

O eSocial visa a unificação e uniformização das informações a serem enviadas pelas empresas, que serão armazenadas em uma única base de dados do governo. Com esta base, os dados serão processados e serão geradas, no próprio ambiente do governo, as informações para fins previdenciários, fiscais com apuração de tributos e FGTS.  
   
O eSocial detalhará as informações da folha de pagamento de todas as empresas, incluindo todos os pagamentos necessários à Previdência Social e independente do porte ou faturamento, abrangendo também as informações do Livro de Registro de empregados.   
   
Os dados da Folha Digitalizada e Registro de Empregados serão armazenados em um cadastro único, e compartilhados por várias entidades do governo: Receita Federal, Ministério do Trabalho, Previdência Social e Justiça do Trabalho.   
   
Veja o Manual de Orientação das informações a serem enviadas para o governo em:  
   
[{+}](http://www.esocial.gov.br/doc/Manual%20de%20Orientacao%20do%20eSocial%20_%20versao%201.0.pdf)<http://www.esocial.gov.br/doc/Manual%20de%20Orientacao%20do%20eSocial%20_%20versao%201.0.pdf+><http://www.esocial.gov.br/doc/Manual%20de%20Orientacao%20do%20eSocial%20_%20versao%201.0.pdf>  
   
Para a geração dos arquivos a serem enviados será necessário executar o wizard de Gerar Carga Inicial.  
   
Através deste módulo serão geradas as cargas do eSocial, conforme leiaute dos arquivos que compõem o Sistema de Escrituração Fiscal Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (eSocial), que será exigido para os eventos ocorridos a partir da competência de janeiro de 2014.

Atenção: Caso existam eventos de tabela na fila de eventos, independente do tipo da operação ou status, estes não serão considerados neste processo.  
   
Considerações importantes na geração dos arquivos:   
S-1000 - Informações do Empregador  
S-1020 - Tabela de Lotações Tributárias  
S-1030 - Tabela de Cargos  
S-1050 - Tabela de Horários/Turnos de Trabalho  
S-1060 - Tabela de Estabelecimento/Obras  
S-2200 - Evento Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador
