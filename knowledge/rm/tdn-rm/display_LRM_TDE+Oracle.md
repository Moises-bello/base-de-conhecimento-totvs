---
content_hash: d9f0a5fb829d5fbb9b44d023abd04c1a44542a7c3249d6411c1c65b74756b3be
fetched_at: '2026-06-29T00:10:38.157520+00:00'
page_id: '544178878'
product: rm
source: tdn-rm
title: TDE Oracle
type: documentation
url: https://tdn.totvs.com/display/LRM/TDE+Oracle
version: 17
---

O **TDE** (Transparent Data Encryption) para **Oracle** é uma ferramenta de criptografia de mídia do banco de dados , disponível a partir da versão **10g Release**. De acordo com a [documentação disponibilizada pela Oracle](https://docs.oracle.com/database/121/ASOAG/introduction-to-transparent-data-encryption.htm#ASOAG10117), o **TDE** performa a criptografia e "descriptografia" de I/O em tempo real dos dados e arquivos de *log*. Ele utiliza uma chave para criptografia da *database* **DEK** (Database Encryption Key), armazenada no registro de *boot* da *database* para disponibilidade durante a recuperação. 

Esta ferramenta foi estudada e testada para verificar a viabilidade de seu uso no produto **RM**, para que este esteja apto, caso o cliente queria atender algum item de gerenciamento/segurança, de dados como a **Lei Geral de Proteção de Dados** (LGPD).

# Ambiente Operacional

Em nossos testes de performance, utilizamos a criptografia dos table\_spaces dos esquemas RM e TOTVSAUDIT nas rotinas de recálculo do espelho do cartão, geração do espelho do ponto e conversão da base de dados 'Exemplo' (disponível para download em nossa central de Download). Tais processos foram repetidos na portabilidade  descrita abaixo, bem como o método adotado para parametrização e os tempos apurados nas execuções.

* Sistema Operacional Windows 10 Pro 64bits
* Processador Intel Core i5-7200U CPU 2.50GHz 2.71 GHz
* Memória RAM 16GB
* HD SSD

Os resultados coletados foram examinados por um método de análise de performance de *software*, o **AWR (Automatic Workload Repository)**
