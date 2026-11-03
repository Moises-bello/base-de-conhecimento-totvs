---
content_hash: e8217cb883600c62445f7dbfada7ba93148044b496b922fbe48910603dab5ab8
fetched_at: '2026-06-29T00:09:44.425487+00:00'
page_id: '433236712'
product: rm
source: tdn-rm
title: Diferença entre RM.Host e RM.Host.Service
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=433236712
version: 4
---

# Indice

---

# Informações

---

O RM apresenta duas formas de se iniciar o host para utilização do sistema: o RM.Host.exe ou o RM.Host.Service.exe.  
Quando iniciamos o host através do RM.Host.Service.exe, o host é iniciado como um serviço, possibilitando os controles que são realizados pelo sistema operacional. Já o RM.Host.exe inicia o host como um executável.

A seguir, segue algumas diferenças entre iniciar o host como um serviço ou como um executável.

### RM.Host.Service.exe

• Ele é controlado pelo sistema operacional e sobe como serviço do windows. Com isso o RM.Host.Service possui as facilidades dos serviços desse tipo, como a visualização de eventos pelo Event Viewer.

• É iniciado junto com o Windows e quando há alguma falha ele é reiniciando juntamente com o Windows. Dessa forma, torna-se mais estável do que quando é iniciado como um executável (RM.Host).

• O próprio instalador é preparado para utilizar o RM.Host.Service.

• Trabalhando como um serviço, possui maior controle sobre a segurança e controle de acesso.

• Sua utilização é facilitada para utilização de ambiente em 3 camadas, deixando transparente a divisão de jobs e utilização do pool além de ter seu arquivo de configuração estruturado para tratar o ambiente como 3 camadas.

• É recomendado pela TOTVS.

### RM.Host.exe:

• Funciona como um executável e o usuário de execução será o usuário logado na máquina.  
Entretanto, se o cliente estiver em ambiente local e optar por usá-lo, não há nada que o impeça e o sistema irá funcionar normalmente.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Diferença entre RM.Host e RM.Host.Service

falsefalse

**Status:** Finalizado

false

**Data:** 05/11/2018

false

**Autores:**
