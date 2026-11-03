---
content_hash: d540fca55ec1bbee366e4834100e3b41eda110a1b5b6cb9d94110a0aaddcddff
fetched_at: '2026-06-29T00:08:23.084398+00:00'
page_id: '269444755'
product: rm
source: tdn-rm
title: Erro no Hardlock - Gerenciamento de Config
type: documentation
url: https://tdn.totvs.com/display/LRM/Erro+no+Hardlock+-+Gerenciamento+de+Config
version: 7
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

O objetivo deste documento é trazer uma visão da funcionalidade "Gerenciamento de Config".

## **02. EXEMPLO DE UTILIZAÇÃO**

License Sever - **HardLock**

       A inconsistência informada no print pode ser solucionada verificando se o  nome dos arquivos de licença estão corretos, conforme a seguir : (totvslic.key e applylic.key). Se por ventura estiver diferente, renomeio-os.

       Outra situação que pode ocasionar esse erro é o fato do Hardlcok está com problemas de conectividade. Certifica-se que  o hardlock está a com a luz de led acesa.

       Após isso edite o arquivo smartclient.ini do diretorio C:\totvs\totvslicense2014\bin\monitor\smartclient e confira se está com as mesmas informações como abaixo, senão estiver, altere , salve e teste novamente.

 

xmlObservação

       Não esquecer de verificar se o Hardlock está plugado corretamente na máquina e se o mesmo está com a luz de led acesa.

false

**Versão:** 12.1.14
