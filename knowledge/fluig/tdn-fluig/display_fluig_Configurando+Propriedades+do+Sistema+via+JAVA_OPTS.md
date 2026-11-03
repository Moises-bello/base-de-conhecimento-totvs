---
content_hash: 0820edcca2ab42a74b7c7e058dba7ac20c97b974577f2aaed01ea2b4e72920dd
fetched_at: '2026-06-28T21:35:17.284896+00:00'
page_id: '1040980558'
product: fluig
source: tdn-fluig
title: Configurando Propriedades do Sistema via JAVA_OPTS
type: documentation
url: https://tdn.totvs.com/display/fluig/Configurando+Propriedades+do+Sistema+via+JAVA_OPTS
version: 2
---

4.\*ndice

# Objetivo

---

Este guia visa mostrar ajustar o comportamento do servidor, utilizamos os arquivos de script que preparam o ambiente antes da execução do Java.

# Introdução

---

O comportamento e a performance do Fluig são gerenciados através de scripts de configuração que preparam o ambiente da **Java Virtual Machine (JVM)** antes do servidor subir.

Embora o Fluig compartilhe a mesma lógica de negócio em diferentes plataformas, a forma como ele interage com o Sistema Operacional muda. Por isso, utilizamos os arquivos localizados em `/appserver/bin/` para definir as **Propriedades do Sistema** e parâmetros de memória. Estes arquivos garantem que as personalizações necessárias (como fuso horário, codificação de caracteres e limites de memória) sejam injetadas corretamente na variável `JAVA_OPTS` no momento da inicialização, garantindo a consistência do sistema tanto em ambientes **Windows** quanto **Linux**.

# Localização

---

O arquivo de configuração reside no diretório de binários do servidor (/appserver/bin/). Em ambientes Linux, deve ser utilizado o arquivo standalone.conf. Já em windows, o arquivo standalone.conf.bat.

| **Arquivo** | **Sistema Operacional** | **Formato** |
| --- | --- | --- |
| **`standalone.conf`** | Linux / Unix | Shell Script |
| **`standalone.conf.bat`** | Windows | Batch Script |

# Configurando Propriedades do Sistema via JAVA\_OPTS

---

A variável **`JAVA_OPTS`** é um agrupador de parâmetros. Através dela, definimos as **Propriedades do Sistema** que o Java utilizará globalmente na aplicação. Sempre anexe sua configuração à variável existente para preservar as definições originais do Fluig.

bashNo Linux (standalone.conf)powershellNo Windows (standalone.conf.bat)

# Observações

---

* **Sintaxe:** Toda Propriedade do Sistema deve ser precedida pelo prefixo `-D`.
* **Memória:** Parâmetros como `-Xms` (mínimo) e `-Xmx` (máximo) também são inseridos no `JAVA_OPTS`, embora tecnicamente sejam flags de memória da JVM e não propriedades customizadas.
* **Reinicialização:** Qualquer alteração nestes arquivos exige a **reinicialização** do Fluig para entrar em vigor.
